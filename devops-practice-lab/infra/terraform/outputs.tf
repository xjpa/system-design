output "public_ip" {
  description = "Short-lived host address for inventory and smoke tests"
  value       = aws_instance.host.public_ip
}

output "api_url" {
  value = "http://${aws_instance.host.public_ip}:8080"
}

output "instance_id" {
  value = aws_instance.host.id
}
