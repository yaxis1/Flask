# We need a EC2 instance to launch a docker that in turn launches a ubuntu with jenkins.

# Cloud infrastructure for the flask app
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "eu-west-3"
  access_key = ""
  secret_key = ""
}

#VPC - importing from console
#terraform import aws_vpc.GODZILLA_VPC vpc-0a4bc76672e4052c7
resource "aws_vpc" "GODZILLA_VPC" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "GODZILLA_VPC"
  }
  } 

# Internet Gateway attached to above vpc
resource "aws_internet_gateway" "GODZILLA_IGW" {
  vpc_id = aws_vpc.GODZILLA_VPC.id
  tags = {
    Name = "GODZILLA_IGW"
  }
}

# Route  table
resource "aws_route_table" "public_route" {
  vpc_id = aws_vpc.GODZILLA_VPC.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.GODZILLA_IGW.id 
    }

  route {
    ipv6_cidr_block = "::/0"
    gateway_id = aws_internet_gateway.GODZILLA_IGW.id
  }
  
  tags = {
    Name = "godzilla_route_public"
  }
  
}

/* resource "aws_route_table" "private_route" {
  vpc_id = aws_vpc.GODZILLA_VPC.id

  route {
    cidr_block = "10.0.1.0/24"
    gateway_id = aws_nat_gateway.mynat.id
    }
  
  tags = {
    Name = "godzilla_route_private"
  }
  
}
 */

# Public Subnet
resource "aws_subnet" "public_subnet" {
  vpc_id = aws_vpc.GODZILLA_VPC.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "eu-west-3a"

  tags = {
    Name = "PUBLIC_SUBNET"
  }
} 
 
# Private Subnet
 resource "aws_subnet" "private_subnet" {
  vpc_id = aws_vpc.GODZILLA_VPC.id
  cidr_block = "10.0.2.0/24"

  tags = {
    Name = "PRIVATE_SUBNET"
  }
} 


# Route table association public

resource "aws_route_table_association" "public_route" {
  subnet_id = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_route.id
  
}
# NAT GATEWAY
/* resource "aws_nat_gateway" "mynat" {
  allocation_id = aws_route_table.private_route.id
  subnet_id = aws_subnet.private_subnet.id

}
 */

# Security group
resource "aws_security_group" "web_traffic" {
  name = "allow_web_traffic"
  vpc_id = aws_vpc.GODZILLA_VPC.id

  ingress {
    cidr_blocks = [ "0.0.0.0/0" ]
    description = "HTTPS"
    from_port = 443
    to_port = 443
    protocol = "tcp"
  } 
  ingress {
    cidr_blocks = [ "0.0.0.0/0" ]
    description = "HTTP"
    from_port = 80
    to_port = 80
    protocol = "tcp"
  }

  ingress {
    cidr_blocks = [ "0.0.0.0/0" ]
    description = "SSH"
    from_port = 22
    to_port = 22
    protocol = "tcp"
  }

  ingress {
    cidr_blocks = [ "0.0.0.0/0" ]
    description = "TCP"
    from_port = 8080 # This port will be opened for internet as ec2's 8080 will be joined with docker's 2103(flask)
    to_port = 8080 # ec2ip:8080
    protocol = "tcp"
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0" ]
  } 

  tags = {
    Name = "Allow http, https and ssh"
  }
}

# Network interface with an IP from subnet
resource "aws_network_interface" "SERVER_NIC" {
  subnet_id = aws_subnet.public_subnet.id
  private_ips = [ "10.0.1.49" ]
  security_groups = [ aws_security_group.web_traffic.id ]
  
  # Will be attached to ec2

}

# Elastic ip
resource "aws_eip" "one" {
  vpc = true
  network_interface = aws_network_interface.SERVER_NIC.id
  associate_with_private_ip = "10.0.1.49"
  depends_on = [aws_internet_gateway.GODZILLA_IGW]
}

# EC 2
# Using userscripts to pull source code from github, install and configure docker.
resource "aws_instance" "myec2_from_terraform" {
  ami           = "ami-0d6aecf0f0425f42a"
  instance_type = "t2.micro"
  availability_zone = "eu-west-3a" #Same as public subnet
  key_name = "terraform_access"
  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.SERVER_NIC.id
    
  }

  user_data = <<-EOF
          #! /bin/bash
          sudo apt-get update && sudo apt-get upgrade -y --no-install-recommends
          sudo apt-get -y install docker.io
          sudo apt-get -y install docker-compose

          sudo systemctl start apache2
          sudo systemctl start docker

          mkdir sourcecode
          cd sourcecode
          git clone https://github.com/yaxis1/Flask-jenkins-terraform-docker.git
          cd Flask-jenkins-terraform-docker
          sudo docker build -t theapp .
          sudo docker run -p 8080:2103 theapp 
          EOF
  tags = {
    Name = "server_terraform"
  }
}  





/* resource "aws_route_table_association" "private_route" {
  subnet_id = aws_subnet.private_subnet.id
  route_table_id = aws_route_table.public_route.id
  
} */

#          sudo docker run theapp
         # sudo docker create theapp
         #          sudo apt-get -y install apache2 

         #          echo "<h2> text from TERRA_FORM <h2>" > /var/www/html/index.html
