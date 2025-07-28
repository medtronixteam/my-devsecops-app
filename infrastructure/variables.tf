variable "region" {
  default = "us-east-1"
}

variable "instance_type" {
  default = "t3.micro"
}

variable "ami_id" {
  # Ubuntu 22.04 in us-east-1
  default = "ami-07d9b9ddc6cd8dd30"
}

variable "public_key_path" {
  default = "~/.ssh/deployer.pub"
}

variable "private_key_path" {
  default = "~/.ssh/deployer"
}
