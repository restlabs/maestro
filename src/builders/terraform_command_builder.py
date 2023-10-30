from src.commands.terraform_command import TerraformCommand

class TerraformCommandBuilder:
    def __init__(self):
        self.command_string = "terraform"

    def init(self):
        self.command_string += " init"
        return self

    def plan(self):
        self.command_string += " plan"
        return self

    def apply(self):
        self.command_string += " apply"
        return self

    def add_variable(self, name, value):
        self.command_string += f' -var "{name}={value}"'
        return self

    def build(self):
        return TerraformCommand(self.command_string)
