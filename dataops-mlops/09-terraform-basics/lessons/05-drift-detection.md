# Drift Detection

Drift detection in Terraform is crucial for maintaining the integrity of your infrastructure as code. It ensures that your deployed resources remain consistent with your desired configurations, preventing unexpected issues in production.

## What is Drift?

Drift refers to the divergence between your Terraform configuration and the actual state of your infrastructure. This can happen due to manual changes made outside of Terraform, whether it’s an accidental update by a team member or an automated process that modifies resources. Identifying drift allows you to restore consistency and avoid potential issues down the line.

### Why Drift Detection Matters

- **Stability:** Keeping your infrastructure consistent helps avoid unexpected behavior in applications.
- **Collaboration:** In team environments, drift can lead to confusion and conflicts. Detecting it early ensures everyone is on the same page.
- **Compliance:** Many industries have regulations that require consistent environment configurations. Drift detection helps maintain compliance.

## How to Detect Drift

Terraform provides a built-in command to detect drift. Running `terraform plan` after making changes to your infrastructure can reveal differences between your configuration files and the actual state.

```bash
terraform plan
```

When you execute this command, Terraform compares the current state of your infrastructure with the configuration files and reports any discrepancies. Here’s how you might see drift in action:

```bash
# Output of terraform plan showing drift
Terraform will perform the following actions:

  # aws_instance.example will be updated in-place
  ~ resource "aws_instance" "example" {
      ami           = "ami-12345678"
    ~ instance_type = "t2.micro" -> "t2.small"  # Drift detected
      ...
  }
```

In the example above, the instance type was changed from `t2.micro` to `t2.small` outside of Terraform, leading to a drift that needs to be resolved.

### Remediating Drift

To fix drift, you can either:

1. **Update the Configuration:** Modify your Terraform files to reflect the current state.
2. **Revert Changes:** Use `terraform apply` to revert the resources to match your configuration.

```bash
terraform apply
```

This command will ensure that your infrastructure is brought back in line with your desired state.

## Common pitfalls

- **Ignoring Manual Changes:** Regularly running `terraform plan` is crucial. Failing to do so can lead to untracked changes that complicate deployments.
- **Over-relying on Automation:** While automation is beneficial, it’s important to monitor infrastructure changes made by scripts or other team members to catch drift early.
- **Not Using State Locking:** Without state locking, simultaneous operations can lead to race conditions, resulting in undetected drift.

## In a nutshell

- Drift is the difference between your Terraform configuration and the actual state of your infrastructure.
- Use `terraform plan` to detect drift effectively.
- Remediate drift by updating the configuration or reverting changes with `terraform apply`.
- Regularly monitor for drift to maintain stability and compliance in your infrastructure.
- Be cautious of manual changes and ensure state locking to avoid race conditions.