```markdown
# AWS S3 — Cheatsheet

## [Section 1: IAM Policies]

| Thing              | Syntax                                       | Notes                               |
|--------------------|----------------------------------------------|-------------------------------------|
| Create Bucket       | `aws s3api create-bucket --bucket BUCKET_NAME` | Replace `BUCKET_NAME` with your desired bucket name. |
| List Buckets        | `aws s3api list-buckets`                    | Lists all S3 buckets in the account. |
| Bucket Policy       | `aws s3api put-bucket-policy --bucket BUCKET_NAME --policy '{JSON_POLICY}'` | Use a JSON string for the policy. |

## [Section 2: Lifecycle Tiers]

| Tier         | Syntax                                        | Notes                              |
|--------------|-----------------------------------------------|------------------------------------|
| Standard     | `aws s3 cp FILE s3://BUCKET_NAME/ --storage-class STANDARD` | Default storage class.             |
| Infrequent Access | `aws s3 cp FILE s3://BUCKET_NAME/ --storage-class STANDARD_IA` | For less frequently accessed data. |
| Glacier       | `aws s3 cp FILE s3://BUCKET_NAME/ --storage-class GLACIER` | For archival storage.              |

## [Section 3: Multipart Upload]

```bash
# Initiate multipart upload
UPLOAD_ID=$(aws s3api create-multipart-upload --bucket BUCKET_NAME --key OBJECT_KEY --query UploadId --output text)

# Upload part (repeat for each part)
aws s3api upload-part --bucket BUCKET_NAME --key OBJECT_KEY --part-number PART_NUMBER --body PART_FILE --upload-id $UPLOAD_ID

# Complete multipart upload
aws s3api complete-multipart-upload --bucket BUCKET_NAME --key OBJECT_KEY --upload-id $UPLOAD_ID --multipart-upload file://parts.json
```

## [Section 4: Encryption]

| Encryption Type  | Syntax                                       | Notes                               |
|-------------------|----------------------------------------------|-------------------------------------|
| SSE-S3            | `aws s3 cp FILE s3://BUCKET_NAME/ --sse AES256` | Server-side encryption with S3 managed keys. |
| SSE-KMS           | `aws s3 cp FILE s3://BUCKET_NAME/ --sse aws:kms --sse-kms-key-id KMS_KEY_ID` | Server-side encryption with KMS keys. |

## [Section 5: Athena Integration]

```sql
-- Create table in Athena
CREATE EXTERNAL TABLE IF NOT EXISTS database_name.table_name (
    column1 STRING,
    column2 INT
) 
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://BUCKET_NAME/path/to/data/';
```

## [Gotchas]

- ⚠️ IAM policies must explicitly allow actions on S3 resources. Be specific in your policies.
- ⚠️ Multipart uploads can incur costs if not completed. Always complete or abort uploads.

## [Mental model]

- Data is stored in Buckets.
- Buckets can have Policies (permissions).
- Objects within buckets can be managed with different storage classes and lifecycle rules.
```