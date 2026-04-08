output "db_instance_endpoint" {
  description = "Database endpoint"
  value       = aws_db_instance.this.endpoint
}

output "db_instance_identifier" {
  description = "Database identifier"
  value       = aws_db_instance.this.identifier
}

output "db_security_group_id" {
  description = "Database security group ID"
  value       = aws_security_group.db.id
}