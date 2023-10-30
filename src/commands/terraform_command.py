from src.commands.command import Command

# Concrete Command class - TerraformCommand
class TerraformCommand(Command):
    def __init__(self, command_string):
        self.command_string = command_string

    def execute(self):
        return f"Executing Terraform command: {self.command_string}"
