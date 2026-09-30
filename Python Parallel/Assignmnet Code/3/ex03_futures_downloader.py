from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError
import time

endpoints = [
    ("https://example.com/a", 0.2),
    ("https://example.com/b", 0.4),
    ("https://example.com/c", 0.6),
    ("https://example.com/d.error", 0.3),
    ("https://example.com/e", 0.8),
    ("https://example.com/f", 1.2),
    ("https://example.com/g", 1.5),
    ("https://example.com/h", 0.5),
    ("https://example.com/i.error", 0.7),
    ("https://example.com/j", 0.9),
]

def download_endpoint(url, delay):
    time.sleep(delay)

    if url.endswith(".error"):
        raise ConnectionError(f"Connection failed: {url}")

    payload = f"Downloaded payload from {url}"
    return payload

with ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = {
        executor.submit(download_endpoint, url, delay): url
        for url, delay in endpoints
    }

    for future in as_completed(future_to_url):
        url = future_to_url[future]

        try:
            payload = future.result(timeout=1.0)
            print(f"SUCCESS: {url} -> {len(payload.encode())} bytes")
        except ConnectionError as exc:
            print(f"ERROR: {url} -> {exc}")
        except TimeoutError:
            print(f"TIMEOUT: {url} took longer than 1 second")
        except Exception as exc:
            print(f"ERROR: {url} -> {exc}")
