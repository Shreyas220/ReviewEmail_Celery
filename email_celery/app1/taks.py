from celery.decorators import tasks

@tasks(name="send_review_email_task")