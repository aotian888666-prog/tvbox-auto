import json

def load_sources():
    with open("config/sources.json","r",encoding="utf-8") as f:
        return json.load(f)

def get_sources():
    return load_sources()
