```markdown
# dbt Transformations — Cheatsheet

## [Core syntax]

| Thing                     | Syntax                                      | Notes                                           |
|---------------------------|---------------------------------------------|-------------------------------------------------|
| Model definition           | `{{ config(materialized='table') }}`      | Defines how the model is materialized (table/view). |
| Reference another model    | `{{ ref('model_name') }}`                  | Use this to refer to another model in dbt.     |
| Source definition          | `source('source_name', 'table_name')`     | Defines a source table for your models.         |
| Test a column              | `dbt test --models model_name`             | Run tests defined in the model.                 |
| Snapshot definition        | `{{ snapshot('snapshot_name') }}`         | Create snapshots for historical data tracking.  |
| Macro usage                | `{{ my_macro(arg1, arg2) }}`               | Call a custom macro defined in dbt.             |

## [Common operations]

```sql
-- Creating a model
{{ config(materialized='view') }}

SELECT 
    id,
    name,
    created_at
FROM 
    {{ source('my_source', 'my_table') }}
WHERE 
    created_at >= '2023-01-01';

-- Defining a test
-- tests/test_unique_id.sql
SELECT 
    id
FROM 
    {{ ref('my_model') }}
GROUP BY 
    id
HAVING 
    COUNT(*) > 1;

-- Creating a snapshot
{% snapshot my_snapshot %}
    {{ config(target_schema='snapshots') }}

    SELECT 
        id,
        name,
        updated_at
    FROM 
        {{ source('my_source', 'my_table') }}

{% endsnapshot %}
```

## [Gotchas]

- ⚠️ Make sure to run `dbt run` after changes to models to apply transformations.
- ⚠️ Snapshots only track changes when a specified unique key is present; ensure your data has it.
- ⚠️ Referring to models before they're built can cause failures; always check dependencies.

## [Mental model]

- **Models transform raw data → Sources provide raw data → Tests ensure data integrity → Snapshots save historical state.**
- **dbt orchestrates this flow, allowing for clear dependency management and modular transformations.**
- **Keep an eye on the materialization strategy to optimize performance and storage.**
```