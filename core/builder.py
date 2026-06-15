import json
import requests
from core.speed_test import test_speed

def build():
    with open("config/sources.json","r",encoding="utf-8") as f:
        sources = json.load(f)

    results = []

    for s in sources:
        speed = test_speed(s["url"])
        if speed < 5:  # filter slow/invalid
            try:
                r = requests.get(s["url"], timeout=5)
                if r.status_code == 200:
                    results.append({
                        "key": s["name"],
                        "name": s["name"],
                        "type": 3,
                        "api": s["url"],
                        "speed": speed,
                        "searchable": 1,
                        "quickSearch": 1
                    })
            except:
                pass

    results = sorted(results, key=lambda x: x["speed"])

    output = {
        "sites": results,
        "lives": [],
        "flags": ["youku","qq","iqiyi"],
        "parse": [],
        "spider": ""
    }

    with open("api/tvbox.json","w",encoding="utf-8") as f:
        json.dump(output,f,ensure_ascii=False,indent=2)

    print("done")
