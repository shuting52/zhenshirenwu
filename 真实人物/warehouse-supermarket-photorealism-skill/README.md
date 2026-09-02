# Warehouse Supermarket Photorealism Skill

## 目录

- `SKILL.md`：核心规则
- `references/`：提示词架构与质量检查
- `scripts/`：校验与 Prompt 编译脚本
- `templates/`：需求采集表、输出模板与 JSON 示例

## 快速使用

校验：

```bash
python scripts/validate_skill.py SKILL.md
```

编译：

```bash
python scripts/prompt_compiler.py templates/example-input.json
```
