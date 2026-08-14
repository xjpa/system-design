variable "aws_region" {
  description = "AWS region for the short-lived lab"
  type        = string
  default     = "ap-southeast-1"
}

variable "environment" {
  description = "Environment label used in names and tags"
  type        = string
  default     = "study"
}

variable "admin_cidr" {
  description = "Your current public IPv4 address as a /32; never use 0.0.0.0/0"
  type        = string
  validation {
    condition     = can(cidrhost(var.admin_cidr, 0)) && var.admin_cidr != "0.0.0.0/0"
    error_message = "admin_cidr must be a valid restricted CIDR, not 0.0.0.0/0."
  }
}

variable "ssh_public_key" {
  description = "Public half of a disposable SSH key used only for this lab"
  type        = string
  sensitive   = true
}

variable "instance_type" {
  description = "Small instance type; verify current regional price before apply"
  type        = string
  default     = "t3.micro"
}

variable "budget_email" {
  description = "Optional email for a USD 5 account budget; blank disables creation"
  type        = string
  default     = ""
}
