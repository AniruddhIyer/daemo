from csp.celery import app as celery_app
from django.db import connection
from crowdsourcing.models import Worker, TaskWorker, PayPalPayoutLog
from crowdsourcing.utils import PayPalBackend
from django.utils import timezone


@celery_app.task
def expire_tasks():
    cursor = connection.cursor()
    query = '''
            WITH taskworkers AS (
                SELECT
                  tw.id
                FROM crowdsourcing_taskworker tw
                INNER JOIN crowdsourcing_task t ON  tw.task_id = t.id
                INNER JOIN crowdsourcing_project p ON t.project_id = p.id
                WHERE p.timeout IS NOT NULL AND tw.created_timestamp + p.timeout * INTERVAL '1 minute' < NOW()
                AND tw.task_status=%(in_progress)s)
                UPDATE crowdsourcing_taskworker tw_up SET task_status=%(expired)s
            FROM taskworkers
            WHERE taskworkers.id=tw_up.id
        '''
    cursor.execute(query, {'in_progress': TaskWorker.STATUS_IN_PROGRESS, 'expired': TaskWorker.STATUS_EXPIRED})
    return 'SUCCESS'

@celery_app.task
def pay_workers():
    workers = Worker.objects.all()
    total = 0

    for worker in workers:
        tasks = TaskWorker.objects.values('task__project__price', 'id').filter(worker=worker,
                                                                               task_status=TaskWorker.STATUS_ACCEPTED,
                                                                               is_paid=False)
        total = sum(tasks.values_list('task__project__price', flat=True))
        if total > 0 and worker.profile.paypal_email is not None and single_payout(total, worker):
            tasks.update(is_paid=True)

    return {"total": total}


def single_payout(amount, worker):
    backend = PayPalBackend()

    payout = backend.paypalrestsdk.Payout({
        "sender_batch_header": {
            "sender_batch_id": "batch_worker_id__" + str(worker.id) + '_week__' + str(timezone.now().isocalendar()[1]),
            "email_subject": "Daemo Payment"
        },
        "items": [
            {
                "recipient_type": "EMAIL",
                "amount": {
                    "value": amount,
                    "currency": "USD"
                },
                "receiver": worker.profile.paypal_email,
                "note": "Your Daemo payment.",
                "sender_item_id": "item_1"
            }
        ]
    })
    payout_log = PayPalPayoutLog()
    payout_log.worker = worker
    if payout.create(sync_mode=True):
        payout_log.is_valid = payout.batch_header.transaction_status == 'SUCCESS'
        payout_log.save()
        return payout_log.is_valid
    else:
        payout_log.is_valid = False
        payout_log.response = payout.error
        payout_log.save()
        return False
