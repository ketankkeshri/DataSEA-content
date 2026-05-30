# Multipart Upload

Multipart upload in AWS S3 is a powerful feature that allows you to upload large files in smaller, manageable parts. This is crucial for data engineers and analysts who deal with vast amounts of data, as it enhances reliability and efficiency in data transfers.

## What is Multipart Upload?

Multipart upload enables you to split a large file into smaller chunks, which can be uploaded independently. This helps in several ways:

- **Improved Speed:** You can upload parts in parallel, reducing the overall upload time.
- **Resilience:** If an upload fails, you can retry only the failed parts instead of starting over.
- **Large File Support:** S3 has a limit of 5GB for single uploads, but multipart allows you to upload files up to 5TB.

Here's how to initiate a multipart upload using the AWS SDK for Python (Boto3):

```python
import boto3

s3 = boto3.client('s3')

# Start a multipart upload
response = s3.create_multipart_upload(Bucket='my-bucket', Key='large-file.txt')

upload_id = response['UploadId']
print(f'Started multipart upload with ID: {upload_id}')
```

## Uploading Parts

Once you have initiated a multipart upload, you can upload each part. Each part must be at least 5MB, except for the last part. Here's how to upload parts:

```python
# Upload a part
part_number = 1
with open('large-file-part1.txt', 'rb') as data:
    response = s3.upload_part(
        Bucket='my-bucket',
        Key='large-file.txt',
        PartNumber=part_number,
        UploadId=upload_id,
        Body=data
    )

print(f'Uploaded part {part_number}, ETag: {response["ETag"]}')
```

You can repeat this process for each part of your file. After uploading all parts, you need to complete the multipart upload.

## Completing Multipart Upload

After uploading all parts, you must finalize the upload by providing a list of the uploaded parts:

```python
# Complete the multipart upload
parts = [
    {'ETag': '<ETag of part 1>', 'PartNumber': 1},
    {'ETag': '<ETag of part 2>', 'PartNumber': 2},
    # Add additional parts here
]

response = s3.complete_multipart_upload(
    Bucket='my-bucket',
    Key='large-file.txt',
    UploadId=upload_id,
    MultipartUpload={'Parts': parts}
)

print(f'Completed multipart upload: {response}')
```

## Common pitfalls

- **Part Size Limit:** Remember, every part must be at least 5MB (except the last one). Trying to upload smaller parts will result in an error.
- **Concurrency Issues:** If you upload parts in parallel, ensure you handle responses properly to avoid race conditions with part numbers.
- **Incomplete Uploads:** Failing to call `complete_multipart_upload` will leave your upload in a pending state, consuming S3 resources.

## In a nutshell

- Multipart upload allows you to upload large files in chunks.
- It improves upload speed and resilience.
- Each part must be 5MB or larger, except for the last part.
- Always complete the multipart upload to avoid dangling uploads.
- Handle parts and errors carefully, especially with concurrent uploads.