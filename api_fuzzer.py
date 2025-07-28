import requests

import sys

def come_back_always():
    for word in sys.stdin:
        res = requests.get(url=f"Target URL/{word}")
        if res.status_code == 404:
            come_back_always()
        else:
            data = res.json()
            print(data)
            print(res.status_code)
            print(word)

come_back_always()