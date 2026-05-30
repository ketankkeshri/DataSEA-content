```markdown
# Feature Store Architecture (Feast) — Cheatsheet

## [Section 1: DataOps + MLOps Concepts]

| Thing                | Syntax                              | Notes                                                        |
|----------------------|-------------------------------------|--------------------------------------------------------------|
| Feature Store        | `feast.FeatureStore`                | Centralized repository for features.                         |
| Online Store         | `feast.types.OnlineStore`           | Stores features for real-time access.                        |
| Batch Store          | `feast.types.BatchStore`            | Stores features for batch processing.                        |
| Registry             | `feast.Registry`                     | Manages feature definitions and metadata.                   |
| Deployment Patterns   | `feast.Deployment`                  | Strategies for deploying features to production.            |

## [Common Operations]

```python
# Initialize the Feature Store
import feast

fs = feast.FeatureStore(repo_path="path/to/feature_repo")

# Define a feature view
from feast import FeatureView, Entity, Field

entity = Entity(name="customer_id", join_key="customer_id")
feature_view = FeatureView(
    name="customer_features",
    entities=[entity],
    features=[
        Field(name="spend", dtype="FLOAT"),
        Field(name="last_purchase", dtype="TIMESTAMP")
    ],
    ttl=86400,  # Time-to-live for features
)

# Register the feature view
fs.apply([feature_view])

# Fetch features for online use
features = fs.get_online_features(
    feature_refs=["customer_features:spend", "customer_features:last_purchase"],
    entity_rows=[{"customer_id": "123"}]
).to_dict()
```

## [Gotchas]

- ⚠️ Ensure the feature definitions in the registry match the data types in your online and batch stores.
- ⚠️ Watch out for TTL expirations; features may become stale if not refreshed properly.
- ⚠️ Always validate your feature retrieval logic to avoid serving incorrect data in production.

## [Mental model]

1. **Feature Store**: Central hub for feature management.
2. **Online vs. Batch**: Real-time access vs. scheduled batch retrievals.
3. **Registry**: The single source of truth for feature definitions and metadata.
```