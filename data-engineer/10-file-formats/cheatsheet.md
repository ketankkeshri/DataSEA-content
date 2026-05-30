```markdown
# Big Data File Formats — Cheatsheet

## Data Engineering

| Format  | Extension | Use Case                              | Key Features                          |
|---------|-----------|---------------------------------------|---------------------------------------|
| Parquet | `.parquet`| Columnar storage for analytics        | Efficient for complex queries, supports nested data. |
| Avro    | `.avro`   | Row-based storage, schema evolution   | Dynamic schema, great for data serialization. |
| ORC     | `.orc`    | Optimized for read-heavy workloads    | High compression, supports complex data types. |
| JSON    | `.json`   | Human-readable data interchange        | Simple structure, widely used in APIs. |
| Binary  | `.bin`    | Compact representation of data        | Faster read/write, not human-readable. |

## Common Operations

### Parquet Example
```python
import pandas as pd

# Write DataFrame to Parquet
df.to_parquet('data.parquet')

# Read Parquet file
df = pd.read_parquet('data.parquet')
```

### Avro Example
```python
import fastavro

# Write to Avro
with open('data.avro', 'wb') as out:
    fastavro.writer(out, schema, records)

# Read Avro file
with open('data.avro', 'rb') as inp:
    records = fastavro.reader(inp)
```

### ORC Example
```python
import pyarrow as pa
import pyarrow.orc as orc

# Write DataFrame to ORC
table = pa.Table.from_pandas(df)
orc.write_table(table, 'data.orc')

# Read ORC file
table = orc.read_table('data.orc')
df = table.to_pandas()
```

## Gotchas

- ⚠️ Parquet is not ideal for small files; prefer Avro for smaller datasets.
- ⚠️ ORC files may not be compatible with all data processing engines; check compatibility.

## Mental model

- **Parquet**: Columnar, fast for analytics.
- **Avro**: Schema evolution, great for streaming.
- **ORC**: Optimized for read, complex data support.
```