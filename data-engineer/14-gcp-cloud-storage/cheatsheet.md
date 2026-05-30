```markdown
# GCP Cloud Storage — Cheatsheet

## [Section 1: Core Concepts]

| Thing          | Syntax                                    | Notes                                         |
|----------------|-------------------------------------------|-----------------------------------------------|
| Bucket         | `gsutil mb gs://bucket-name`             | Create a new bucket.                          |
| List Buckets   | `gsutil ls`                               | List all buckets in your project.            |
| Upload File    | `gsutil cp localfile gs://bucket-name/`  | Upload a file to a bucket.                    |
| Download File  | `gsutil cp gs://bucket-name/file localfile` | Download a file from a bucket.                |
| Delete Bucket  | `gsutil rb gs://bucket-name`             | Remove a bucket (must be empty).              |

## [Section 2: IAM & Permissions]

| Permission     | Role                                       | Notes                                         |
|----------------|--------------------------------------------|-----------------------------------------------|
| Read Access    | `Storage Object Viewer`                    | Allows reading objects in the bucket.        |
| Write Access   | `Storage Object Creator`                   | Allows uploading objects to the bucket.      |
| Admin Access   | `Storage Admin`                            | Full control over the bucket and its contents.|

## [Section 3: Lifecycle Management]

```json
{
  "lifecycle": {
    "rule": [
      {
        "action": { "type": "Delete" },
        "condition": { "age": 365 }
      }
    ]
  }
}
```
- Apply to bucket using `gsutil lifecycle set lifecycle.json gs://bucket-name`.

## [Section 4: Signed URLs]

```python
from google.cloud import storage
from datetime import timedelta

client = storage.Client()
bucket = client.bucket('bucket-name')
blob = bucket.blob('file-to-access')

url = blob.generate_signed_url(
    version='v4',
    expiration=timedelta(minutes=15),
    method='GET'
)
```
- Use signed URLs for temporary access to private files.

## [Section 5: Integration with BigQuery]

```sql
CREATE EXTERNAL TABLE `project.dataset.table`
OPTIONS (
  format = 'CSV',
  uris = ['gs://bucket-name/file.csv']
);
```
- Query data directly from Cloud Storage into BigQuery.

## [Gotchas]

- ⚠️ Buckets must have unique names globally across GCP.
- ⚠️ IAM changes may take a few minutes to propagate.

## [Mental model]

- **Buckets** are containers for storing objects.
- **Objects** are the files you upload to buckets.
- **Lifecycle Rules** automate the management of objects over time.
```