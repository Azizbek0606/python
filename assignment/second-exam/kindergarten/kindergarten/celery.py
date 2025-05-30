import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kindergarten.settings")

app = Celery("kindergarten")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.broker_url = "redis://localhost:6379/0"
app.conf.result_backend = "redis://localhost:6379/0"
app.conf.result_expires = 604800  # 7 kun

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "generate-monthly-report": {
        "task": "inventory.tasks.generate_monthly_report",
        "schedule": 2592000.0,  # 30 kun
    },
    "update-portion-estimates": {
        "task": "inventory.tasks.update_portion_estimates",
        "schedule": 86400.0,  # 1 kun
    },
}