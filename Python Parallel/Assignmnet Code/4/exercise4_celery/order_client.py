"""Celery client demonstrating independent tasks and a task chain."""

import time

from celery import chain

from tasks import validate_order, calculate_tax_and_discount, generate_invoice_pdf


def monitor_result(async_result):
    print(f"Task Dispatched: {async_result.id}")

    while not async_result.ready():
        print(".", end="", flush=True)
        time.sleep(0.5)

    print()
    if async_result.successful():
        result = async_result.get()
        print("Task Result:", result)
        return result

    print("Task failed:", async_result.failed())
    return None


def main():
    print("\n--- INDEPENDENT ASYNCHRONOUS TASKS ---")

    orders = [
        ("ORD-101", ["Item A", "Item B"], 250.0),
        ("ORD-102", ["Keyboard", "Mouse"], 150.0),
        ("ORD-103", ["Monitor"], 300.0),
    ]

    results = []
    for order_id, items, amount in orders:
        async_result = validate_order.delay(order_id, items, amount)
        results.append(async_result)

    for result in results:
        monitor_result(result)

    print("\n--- SEQUENTIAL CELERY CHAIN ---")

    order_pipeline = chain(
        validate_order.s("ORD-202", ["Laptop", "Mouse"], 1200.0)
        | calculate_tax_and_discount.s(tax_rate=0.18)
        | generate_invoice_pdf.s(customer_email="customer@example.com")
    )

    chain_result = order_pipeline.apply_async()
    print("Pipeline submitted! Waiting for final invoice...")
    final_msg = chain_result.get()
    print("Pipeline Output:", final_msg)


if __name__ == "__main__":
    main()
