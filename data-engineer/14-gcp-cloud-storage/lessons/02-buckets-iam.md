# Buckets IAM

Managing access permissions in Google Cloud Storage (GCS) buckets is crucial for data engineers. Properly setting IAM (Identity and Access Management) roles ensures that the right users and services can access your data, while keeping it secure from unauthorized access. 

## Understanding IAM Roles in GCS

IAM roles are collections of permissions that define what actions a user or service account can perform on GCS resources. GCS offers predefined roles like `roles/storage.admin`, `roles/storage.objectViewer`, and `roles/storage.objectCreator`. Each of these roles grants a different level of access.

For example, if you want a user to upload files to a bucket but not delete them, you would assign them the `roles/storage.objectCreator` role. Here’s how to set this up using the `gcloud` command-line tool:

```bash
# Assign the object creator role to a user
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member='user:example@example.com' \
  --role='roles/storage.objectCreator'
```

This command binds the `objectCreator` role to the specified user for the project associated with your GCS bucket.

## Custom IAM Roles

Sometimes, the predefined roles might not fit your specific use case. In such situations, you can create custom IAM roles. Custom roles allow you to specify granular permissions tailored to your needs.

To create a custom role, you can use the `gcloud` command as follows:

```bash
# Create a custom role
gcloud iam roles create CustomBucketRole \
  --project=YOUR_PROJECT_ID \
  --title="Custom Bucket Role" \
  --description="Custom role for specific bucket permissions" \
  --permissions='storage.objects.create,storage.objects.get,storage.objects.delete'
```

In this example, `CustomBucketRole` allows users to create, read, and delete objects in a bucket. 

### Granting Access to Service Accounts

Service accounts are often used by applications or services to access GCS resources programmatically. Granting IAM roles to service accounts follows the same principles as granting them to users.

Here’s how to grant a service account the `roles/storage.objectViewer` role:

```bash
# Assign the object viewer role to a service account
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member='serviceAccount:your-service-account@YOUR_PROJECT_ID.iam.gserviceaccount.com' \
  --role='roles/storage.objectViewer'
```

This way, your application can read objects from the bucket without compromising security by exposing unnecessary permissions.

## Common pitfalls

- **Over-permissioning:** Avoid granting broad roles like `roles/storage.admin` unless absolutely necessary. It’s better to follow the principle of least privilege.
- **Not using service accounts:** Relying on user accounts for application access can lead to security issues and difficulty in managing permissions.
- **Failing to audit permissions:** Regularly review IAM roles to ensure users and service accounts have appropriate access, especially after team changes.

## In a nutshell

- IAM roles control access to GCS buckets and objects.
- Use predefined roles for common access patterns but consider custom roles for specific needs.
- Grant roles to service accounts for secure and manageable access.
- Avoid over-permissioning and conduct regular audits to maintain security.