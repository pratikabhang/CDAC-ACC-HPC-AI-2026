from celery import Celery

app = Celery(
    "demo",
    broker="amqp://guest:guest@localhost:5672//",
    backend="rpc://",
    include=["celery_tasks"]
)

app.conf.update(
    task_serializer="json",
    result_serializer="json",
    app_content=["json"],
    timezone="Asia/Kolkata",
    enable_utc=True
)