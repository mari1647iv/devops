# Terraform Best Practices

- One Workspace Per Environment Per Terraform Configuration
- Delegate Workspaces
- Enable version control on terraform state files bucket
- Manage multiple Terraform modules and environments with Terragrunt
- Turn on debug when you need do troubleshooting
- Use shared modules
- Isolate environment
- Use `terraform import` to include as many resources you can
- Avoid hard coding the resources
- Validate and format terraform code - `terraform fmt`
- Generate README for each module with input and output variables
- Do not forget to update terraform version
- Run terraform in docker container
- Use pre-installed Terraform plugins
- Use naming convention:
  - Use `_` (underscore) instead of `-` (dash) in all Terraform names
  - Only use lowercase letters and numbers
