import requests
import json
import sys

def come_back_always():
    for word in sys.stdin:
        res = requests.get(url=f"Your URL goes here.{word}")
        # URL example - http://10.10.10.10/
        if res.status_code == 404:
            come_back_always()
        else:
            data = res.json()
            print(word)
            print(res.status_code)
            print(json.dumps(data,indent=4))

come_back_always()

# Make sure to have the correct wordlist while running this tool. 
# How to run
# cat wordlist.txt | python3 api_fuzzer.py