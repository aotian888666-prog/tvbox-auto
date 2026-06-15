import json
import requests

with open("sources/base.json", "r", encoding="utf-8") as f:
    sources = json.load(f)

valid_sites = []

for s in sources:
    try:
        r = requests.get(s["url"], timeout=5)
        if r.status_code == 200:
            valid_sites.append({
                "key": s["name"],
                "name": s["name"],
                "type": 3,
                "api": s["url"],
                "searchable": 1,
                "quickSearch": 1
            })
    except:
        pass

output = {
    "sites": valid_sites,
    "lives": [],
    "flags": ["youku", "qq", "iqiyi"],
    "parse": [],
    "spider": ""
}

os.makedirs("api", exist_ok=True)
with open("api/tvbox.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("done")
