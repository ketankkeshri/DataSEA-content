```markdown
# Terraform Basics — Cheatsheet

## [Section 1: Providers]

| Thing        | Syntax                                  | Notes                                       |
|--------------|-----------------------------------------|---------------------------------------------|
| Define       | `provider "aws" { ... }`               | Specify cloud provider configurations.      |
| Version      | `required_providers { aws = { version = "~> 3.0" } }` | Control provider version compatibility.    |
| Authentication | `access_key = "..."`<br>`secret_key = "..."` | Credentials for accessing AWS services.    |

## [Section 2: State Management]

```hcl
# Backend configuration example
terraform {
  backend "s3" {
    bucket         = "my-tf-state-bucket"
    key            = "terraform.tfstate"
    region         = "us-west-2"
  }
}
```

## [Section 3: Modules]

| Thing            | Syntax                                 | Notes                                         |
|------------------|----------------------------------------|-----------------------------------------------|
| Module usage     | `module "example" { source = "./path" }` | Reuse configurations with modules.          |
| Input variables   | `variable "instance_type" { default = "t2.micro" }` | Customize module behavior.                 |
| Output values     | `output "instance_id" { value = aws_instance.example.id }` | Return values from modules.                |

## [Section 4: Drift Detection]

```hcl
# Detect drift in the infrastructure
terraform plan -detailed-exitcode
```

## [Gotchas]

- ⚠️ Remember to run `terraform init` after adding new providers or modules.
- ⚠️ State files are sensitive; use version control with caution.

## [Mental model]

- **Providers**: The bridge between Terraform and your cloud provider.
- **State**: A snapshot of your infrastructure; ensure it's secure and backed up.
- **Modules**: Encapsulate reusable code to streamline your configurations.
```