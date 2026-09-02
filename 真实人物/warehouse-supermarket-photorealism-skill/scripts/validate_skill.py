#!/usr/bin/env python3
from pathlib import Path
import re, sys

required = ["## 目标", "## 适用场景", "## 不适用场景", "## 输入要求",
            "## 执行工作流", "## 输出格式", "## 质量检查", "## 异常处理"]

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("SKILL.md")
text = path.read_text(encoding="utf-8")

checks = [
    ("YAML frontmatter", text.startswith("---")),
    ("name field", bool(re.search(r"^name:\s*[a-z0-9-]+\s*$", text, re.M))),
    ("description field", "description:" in text[:1000]),
] + [(s, s in text) for s in required]

failed = False
for name, ok in checks:
    print(f"[{'OK' if ok else 'FAIL'}] {name}")
    failed = failed or not ok

raise SystemExit(1 if failed else 0)
