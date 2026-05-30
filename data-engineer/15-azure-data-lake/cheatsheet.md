```markdown
# Azure Data Lake Storage — Cheatsheet

## [Section 1: Core Concepts]

| Thing                     | Syntax                                     | Notes                                                |
|---------------------------|--------------------------------------------|------------------------------------------------------|
| Create a Data Lake        | `az storage account create --name <name> --resource-group <group> --location <location> --sku <sku>` | Use `StorageV2` for Gen2 features.                   |
| Enable Hierarchical Namespace | `az storage account update --name <name> --resource-group <group> --enable-hierarchical-namespace true` | Required for Gen2 features.                           |
| Access Control List (ACL) | `az storage fs access set --acl <acl> --path <path> --account-name <account>` | Manage permissions for files and folders.            |

## [Section 2: Common Operations]

```bash
# Uploading a file to Data Lake
az storage fs file upload --account-name <name> --file <local-file-path> --path <file-path> --file-system <filesystem>

# Listing files in a Data Lake
az storage fs file list --account-name <name> --file-system <filesystem> --output table

# Deleting a file
az storage fs file delete --account-name <name> --file-system <filesystem> --path <file-path>
```

## [Gotchas]

- ⚠️ Ensure the storage account is of type `StorageV2` to use Gen2 features.
- ⚠️ Permissions set on the container level may not apply to individual files; check ACLs.

## [Mental model]

- **Gen2 Features:** Hierarchical namespace, ACLs.
- **Storage Types:** Blob storage for unstructured data, Data Lake for analytics.
- **Integration:** Works seamlessly with Azure Synapse Analytics and Azure Data Factory.
```