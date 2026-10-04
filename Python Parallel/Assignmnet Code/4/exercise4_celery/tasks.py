"""Celery tasks for the Order & Invoice Processing System."""

import time

from celery_config import app


@app.task
def validate_order(order_id, items, total_amount):
    if not items:
        raise ValueError("Order must contain at least one item.")

    if total_amount <= 0:
        raise ValueError("Total amount must be greater than 0.")

    time.sleep(1)

    return {
        "order_id": order_id,
        "status": "VALIDATED",
        "items": items,
        "total": float(total_amount),
    }


@app.task
def calculate_tax_and_discount(order_data, tax_rate=0.18):
    total = float(order_data["total"])
    tax = total * float(tax_rate)

    # No discount rule was specified in the assignment, so the final total
    # is calculated as total + tax.
    final_total = total + tax

    updated = dict(order_data)
    updated["tax"] = round(tax, 2)
    updated["final_total"] = round(final_total, 2)
    updated["status"] = "TAX_CALCULATED"
    return updated


@app.task
def generate_invoice_pdf(order_data, customer_email):
    time.sleep(2)

    return (
        f"Invoice #INV-{order_data['order_id']} generated and sent to "
        f"{customer_email}"
    )
