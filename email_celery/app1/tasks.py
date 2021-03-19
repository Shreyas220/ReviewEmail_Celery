from celery.decorators import tasks
from celery.utils.log import get_task_logger

from .email import send_review_email

@tasks(name="send_review_email_task")
logger = get_task_logger(__name__)


@tasks(name = "send_review_email_task")

def send_review_email_task(name, email , review):
    logger.info("Send review email")
    return send_review_email(name,email,review)

 