```markdown
# MinIO Object Storage — Cheatsheet

## [Core syntax]

| Thing                | Syntax                              | Notes                                         |
|----------------------|-------------------------------------|-----------------------------------------------|
| Start MinIO server   | `minio server /data`               | Starts a MinIO server with data directory.   |
| Access key           | `MINIO_ACCESS_KEY=your_access_key`| Set your access key for authentication.      |
| Secret key           | `MINIO_SECRET_KEY=your_secret_key`| Set your secret key for authentication.      |
| Create bucket        | `mc mb myminio/mybucket`           | Creates a new bucket.                         |
| List buckets         | `mc ls myminio`                    | Lists all buckets in MinIO.                  |
| Upload file          | `mc cp localfile.txt myminio/mybucket/` | Uploads a file to a bucket.            |
| Download file        | `mc cp myminio/mybucket/file.txt ./` | Downloads a file from a bucket.           |

## [Common operations]

```bash
# Start MinIO server
minio server /data

# Create a new bucket
mc mb myminio/mybucket

# Set bucket policy (public read access)
mc policy set public myminio/mybucket

# Upload a file
mc cp localfile.txt myminio/mybucket/

# List objects in a bucket
mc ls myminio/mybucket

# Delete a file
mc rm myminio/mybucket/file.txt
```

## [Gotchas]

- ⚠️ Ensure MinIO server is running before executing client commands.
- ⚠️ Bucket names must be globally unique across all MinIO servers.
- ⚠️ Policies are applied at the bucket level and can affect access.

## [Mental model]

- **Buckets**: Think of them as folders in your file system; they hold objects.
- **Objects**: Files stored in buckets; each object has metadata.
- **Policies**: Control access at the bucket level; define who can do what.
```