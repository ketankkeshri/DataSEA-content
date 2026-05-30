```markdown
# Schema Evolution Strategies — Cheatsheet

## Section 1: Key Concepts

| Concept                  | Description                                                                                                                                                     |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schema Evolution         | The process of managing changes to the schema of a dataset over time, ensuring compatibility and integrity of data.                                          |
| Backward Compatibility    | Allows new schema versions to read data written in older schema versions.                                                                                     |
| Forward Compatibility     | Ensures that older schema versions can read data written in newer schema versions.                                                                             |
| Breaking Changes         | Changes that impact the ability to read or write data; can lead to data loss or corruption if not managed properly.                                           |

## Section 2: Schema Evolution Patterns

```python
# Example of backward compatibility in Avro
import fastavro
from fastavro.schema import load_schema

# Load old and new schema
old_schema = load_schema('old_schema.avsc')
new_schema = load_schema('new_schema.avsc')

# Reading old data with new schema
with open('data.avro', 'rb') as f:
    reader = fastavro.reader(f, new_schema)
    for record in reader:
        print(record)
```

## Gotchas

- ⚠️ **Breaking Changes**: Always document schema changes. Use versioning to avoid confusion.
- ⚠️ **Compatibility Testing**: Test both backward and forward compatibility to avoid runtime errors.

## Mental model

- **Schema Evolution**: Think of it as a tree where each version branches off the previous one.
  - New branches (schema versions) must maintain connections to old branches (data compatibility).
  - Regularly assess branches for any breaking changes to ensure smooth transitions.
```