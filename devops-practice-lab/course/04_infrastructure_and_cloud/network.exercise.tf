terraform {
  required_version = ">= 1.6.0"
}

variable "network_cidr" {
  type    = string
  default = "10.50.0.0/16"
  # TODO: add validation that rejects 0.0.0.0/0.
}

locals {
  # TODO: calculate a /24 subnet at network number 1 with cidrsubnet.
  public_subnet = "TODO"
}

output "public_subnet" {
  value = local.public_subnet
}
