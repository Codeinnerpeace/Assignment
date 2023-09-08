#Contains output vars that acn be displayed
output "ec2_machines" {
 # Here * indicates that there are more than one arn because count is 4   
  value = aws_instance.my-machine.*.arn 
}