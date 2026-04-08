aws_region = "eu-west-2"

project_name = "grip-platform"
environment  = "dev"

vpc_cidr = "10.0.0.0/16"

public_subnet_cidrs = [
  "10.0.1.0/24",
  "10.0.2.0/24"
]

private_subnet_cidrs = [
  "10.0.11.0/24",
  "10.0.12.0/24"
]

availability_zones = [
  "eu-west-2a",
  "eu-west-2b"
]

db_name           = "platformdb"
db_username       = "platformadmin"
db_password       = "ChangeMe123456!"
db_instance_class = "db.t3.micro"
allocated_storage = 20