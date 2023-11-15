from src.commands.terraform_command import TerraformCommand

class TerraformCommandBuilder:
    def __init__(self):
        self.command_string = "terraform"

    def init(self, backend_config=None):
        self.command_string += " init"
        if backend_config:
            self.command_string += f' -reconfigure -backend-config={backend_config}'
        return self

    def plan(self, 
             var_file_name: str = None, 
             plan_output_file_name: str = None, 
             destroy: bool = None,
             refresh_only: bool = None,
             refresh_false: bool = None,
             replace: list[str] = None
             ) -> str:
        
        self.command_string += " plan"

        if var_file_name:
            self.command_string += f' -var-file={var_file_name}'

        if plan_output_file_name:
            self.command_string += f' -out={plan_output_file_name}'

        if destroy:
            self.command_string += ' -destroy'

        if refresh_only:
            self.command_string += ' -refresh-only'

        if refresh_false:
            self.command_string += ' -refresh=false'

        if replace:
            for replacement in replace:
                self.command_string += f' -replace={replacement}'

        return self

    def apply(self):
        self.command_string += " apply"
        return self

    def add_variable(self, name, value):
        self.command_string += f' -var "{name}={value}"'
        return self

    def build(self):
        return TerraformCommand(self.command_string)
