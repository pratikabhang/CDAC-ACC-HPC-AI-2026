import asyncio
import time

async def check_database():
    await asyncio.sleep(0.4)
    return {"db": "HEALTHY", "latency_ms": 12}

async def check_redis_cache():
    await asyncio.sleep(0.2)
    return {"cache": "HEALTHY", "latency_ms": 4}

async def check_storage_service():
    await asyncio.sleep(0.6)
    return {"storage": "HEALTHY", "latency_ms": 28}

async def run_health_checks():
    start = time.perf_counter()

    results = await asyncio.gather(
        check_database(),
        check_redis_cache(),
        check_storage_service(),
    )

    elapsed = time.perf_counter() - start

    print("Health check results:")
    for result in results:
        print(result)

    print(f"Total execution time: {elapsed:.3f} seconds")
    print("Expected: approximately 0.6 seconds, not 1.2 seconds.")

asyncio.run(run_health_checks())
