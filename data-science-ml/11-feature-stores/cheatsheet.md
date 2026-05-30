```markdown
# Feature Stores Intro — Cheatsheet

## [Section 1: Why Use Feature Stores]

| Thing                | Notes                                                                 |
|---------------------|-----------------------------------------------------------------------|
| Centralized Storage  | Simplifies feature management across multiple ML models.             |
| Consistency         | Ensures consistent features are used in both training and serving.   |
| Collaboration       | Facilitates collaboration between data scientists and engineers.      |

## [Section 2: Online vs Offline Feature Stores]

| Type          | Use Case                                         | Access Speed       |
|---------------|--------------------------------------------------|--------------------|
| Online        | Real-time model inference                         | Milliseconds        |
| Offline       | Batch processing and model training               | Seconds to minutes  |

## [Section 3: Feast Overview]

```python
# Initialize Feast
from feast import FeatureStore

fs = FeatureStore(repo_path="path/to/feature_repo")

# Define a feature
feature = {
    "name": "user_clicks",
    "value_type": "INT32",
}

# Create an entity
entity = {
    "name": "user_id",
    "value_type": "STRING",
}

# Register feature and entity
fs.apply(entity, feature)
```

## [Section 4: TTL & Staleness]

| Concept   | Description                                                 |
|-----------|-------------------------------------------------------------|
| TTL       | Time-to-live for features; defines how long features are valid. |
| Staleness | Duration after which a feature is considered stale.         |

## [Gotchas]

- ⚠️ Ensure online feature stores are optimized for low latency. High latency can degrade model performance.
- ⚠️ Watch out for stale features; always monitor and refresh features based on TTL to avoid inaccuracies.

## [Mental model]

- Features are stored in a centralized repository (Feature Store).
- Online stores serve real-time requests, while offline stores are for batch processing.
- TTL manages the freshness of features, avoiding stale data issues.
```