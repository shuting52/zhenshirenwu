#!/usr/bin/env python3
import json, sys

ORDER = ["style","subject","face_skin","hair","outfit","pose","product",
         "environment","composition","lighting","photography"]

def parts(data, key):
    value = data.get(key, [])
    return value if isinstance(value, list) else [value]

if len(sys.argv) != 2:
    raise SystemExit("Usage: python prompt_compiler.py input.json")

with open(sys.argv[1], encoding="utf-8") as f:
    data = json.load(f)

prompt = ", ".join(x for k in ORDER for x in parts(data, k) if x)
negative = data.get("negative", [])
negative = negative if isinstance(negative, list) else [negative]

print(json.dumps({
    "prompt": prompt,
    "negative_prompt": ", ".join(negative)
}, ensure_ascii=False, indent=2))
