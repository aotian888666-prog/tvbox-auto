import requests
import time

def test_speed(url):
    try:
        start = time.time()
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return 9999
        return time.time() - start
    except:
        return 9999
