output "instance_public_ip" {
  description = "IP pública de la instancia de la API"
  value       = aws_instance.wine_api.public_ip
}