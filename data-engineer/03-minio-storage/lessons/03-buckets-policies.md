# Buckets Policies

Managing access to your data is critical in any data engineering workflow. In this lesson, we'll dive into MinIO's bucket policies, enabling you to control who can access your stored data and under what conditions.

## Understanding Bucket Policies

Bucket policies in MinIO define the permissions for actions on buckets and objects stored within them. They are similar to AWS S3 bucket policies, allowing you to specify who can access your data.

### Structure of Bucket Policies

Bucket policies are written in JSON format. Each policy consists of one or more statements, specifying the effect (Allow or Deny), actions (like `s3:GetObject`), and resources (the specific buckets or objects).

Here's what a basic bucket policy looks like:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

### Applying a Bucket Policy

You can apply a bucket policy using the MinIO Client (`mc`). Here’s how you can set it up:

1. First, ensure you have the MinIO client installed and configured.

2. Create or edit a policy file, e.g., `read-only-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/your-user"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

3. Apply the policy to your bucket:

```bash
mc policy set-json read-only-policy.json your-minio/your-bucket-name
```

This allows a specific user to read objects from the bucket while denying any other access.

## Managing Permissions

There are several actions you can control using bucket policies:

- `s3:PutObject`: Allows users to upload files.
- `s3:DeleteObject`: Allows users to delete files.
- `s3:ListBucket`: Allows users to list the contents of the bucket.

### Example: Granting Upload Access

Suppose you want to allow a specific user to upload files to your bucket. Here's how you can modify the policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/your-user"
      },
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

## Common pitfalls

- **Overly Permissive Policies**: Avoid using `"Principal": "*"` unless you intentionally want to allow public access.
- **Resource ARN Mistakes**: Ensure your `Resource` ARNs are correct; otherwise, the policy won't take effect.
- **Missing Permissions**: If your application fails to interact with MinIO, double-check if the required actions are included in your policy.

## In a nutshell

- Bucket policies control access to MinIO buckets and objects.
- They are defined in JSON format, specifying effects, actions, and resources.
- Use the MinIO Client (`mc`) to set and manage these policies.
- Always ensure policies are not overly permissive and correctly specify resources.