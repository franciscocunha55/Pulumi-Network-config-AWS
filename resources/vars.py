subnet_private_cidr_block=["10.235.22.0/25", "10.235.22.128/25"]
subnet_public_cidr_block= ["10.235.23.192/28", "10.235.23.208/28"]
availability_zone_names= ["eu-central-1a", "eu-central-1b", "eu-central-1c"]
transit_gateway_id = ""

# SSH Whitelist
sg_ssh_inbound = ["10.0.0.0/16"]

### EC2 IAM Role ###

assume_role_policy_ec2 = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow"
    }
  ]
}

### Route to subnets coming from VPC Module ### 

destination_cidr_block= {'private_subnet_aws_1': "", 'private_subnet_aws_2': '', 'private_subnet_azure': ''}
