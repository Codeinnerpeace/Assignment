#This file contains the code for resources to be build, deleted or updated
resource "aws_instance" "powerfactors" {
  count         = 4
  ami           = var.ami
  instance_type = var.instance_type
  tags = {
    Name = "powerfactors-${count.index}"
  }
}
