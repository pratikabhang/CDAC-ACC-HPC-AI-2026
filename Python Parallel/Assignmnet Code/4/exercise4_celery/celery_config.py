"""Celery configuration using Redis as broker and result backend."""

from celery import Celery

app = Celery(
    "order_system",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)
