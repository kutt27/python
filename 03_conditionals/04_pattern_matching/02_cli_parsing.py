"""
CLI Parsing logic.
"""

from typing import List

def parse_cli_command(command: List[str]) -> str:
    """
    Parses CLI commands using pattern matching.
    
    Args:
        command: List of command parts
    
    Returns:
        Command result
    
    Real-world use case: CLI tool command parsing, task automation.
    """
    match command:
        # deploy command with environment
        case ["deploy", env] if env in ["dev", "staging", "production"]:
            return f"🚀 Deploying to {env}"
        
        # deploy without environment
        case ["deploy"]:
            return "⚠ Environment required: deploy <dev|staging|production>"
        
        # backup with database name
        case ["backup", "database", db_name]:
            return f"💾 Backing up database: {db_name}"
        
        # logs command with optional service
        case ["logs", service, *options]:
            opts_str = f" with options: {options}" if options else ""
            return f"📜 Showing logs for {service}{opts_str}"
        
        # scale command
        case ["scale", service, count] if count.isdigit():
            return f"📊 Scaling {service} to {count} instances"
        
        case ["help" | "--help" | "-h"]:
            return "ℹ Available commands: deploy, backup, logs, scale"
        
        case _:
            return f"❌ Unknown command: {' '.join(command)}"


def demonstrate_cli_parsing() -> None:
    """
    Demonstrates CLI command parsing with list patterns.
    
    Real-world use case: Terminal applications, automation tools.
    """
    commands = [
        ["deploy", "production"],
        ["backup", "database", "users_db"],
        ["logs", "api-service", "--follow", "--tail=100"],
        ["scale", "web-app", "5"],
        ["help"],
        ["unknown", "command"],
    ]
    
    for cmd in commands:
        result = parse_cli_command(cmd)
        cmd_str = " ".join(cmd)
        print(f"  {cmd_str:35} -> {result}")


if __name__ == "__main__":
    demonstrate_cli_parsing()
