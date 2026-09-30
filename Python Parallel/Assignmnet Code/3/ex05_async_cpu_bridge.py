import asyncio

async def heartbeat_ticker():
    try:
        while True:
            print("[Heartbeat] Active and responsive...")
            await asyncio.sleep(0.25)
    except asyncio.CancelledError:
        print("[Heartbeat] Stopped cleanly.")
        raise

def fibonacci_cpu(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

async def main():
    heartbeat_task = asyncio.create_task(heartbeat_ticker())

    try:
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(None, fibonacci_cpu, 35)
        print("Fibonacci(35):", result)
    finally:
        heartbeat_task.cancel()
        try:
            await heartbeat_task
        except asyncio.CancelledError:
            pass

asyncio.run(main())
