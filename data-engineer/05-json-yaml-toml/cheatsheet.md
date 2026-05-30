```markdown
# JSON, YAML, TOML — Cheatsheet

## Core syntax

| Thing          | Syntax                              | Notes                                      |
|----------------|-------------------------------------|--------------------------------------------|
| JSON Object    | `{"key": "value"}`                 | Key-value pairs; keys must be strings.    |
| JSON Array     | `["item1", "item2"]`               | Ordered list of values.                    |
| YAML Mapping    | `key: value`                       | Similar to JSON objects but more readable. |
| YAML Sequence  | `- item1\n- item2`                 | Lists are denoted with a dash (-).         |
| TOML Table     | `[table]`                           | Sections start with brackets.              |
| TOML Key-Value | `key = "value"`                     | Similar to JSON; supports multiline strings.|
| Schema Valid.  | `{"type": "object", "properties": {...}}` | Used with JSON Schema for validation.     |

## Common operations

```python
import json
import yaml
import toml

# JSON example
json_data = '{"name": "Alice", "age": 30}'
data = json.loads(json_data)

# YAML example
yaml_data = """
name: Alice
age: 30
"""
data_yaml = yaml.safe_load(yaml_data)

# TOML example
toml_data = """
name = "Alice"
age = 30
"""
data_toml = toml.loads(toml_data)
```

## Gotchas

- ⚠️ JSON keys must be strings enclosed in double quotes `"`.
- ⚠️ YAML is sensitive to indentation; use spaces, not tabs.
- ⚠️ TOML does not support comments within strings.
- ⚠️ Schema validation can fail silently; always check for errors.

## Mental model

- **JSON**: Key-value pairs, perfect for APIs.
- **YAML**: Human-readable, better for config files.
- **TOML**: Structured like INI files; great for settings.

```plaintext
JSON: { "key": "value" }
YAML: key: value
TOML: key = "value"
```
```