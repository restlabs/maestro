from src.commands.terraform_command import TerraformCommand
from typing import List, Optional


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
            replace: list[str] = None,
            targets: list[str] = None,
            var_inputs: list[str] = None,
            compact_warnings: bool = None,
            detailed_exit_code: bool = None,
            input_false: bool = None,
            json: bool = None,
            lock_false: bool = None
            ) -> str:
        
        self.command_string += " plan"

        options_mapping = {
            'var_file_name': f' -var-file={var_file_name}' if var_file_name else '',
            'plan_output_file_name': f' -out={plan_output_file_name}' if plan_output_file_name else '',
            'destroy': ' -destroy' if destroy else '',
            'refresh_only': ' -refresh-only' if refresh_only else '',
            'refresh_false': ' -refresh=false' if refresh_false else '',
            'replace': f" {' '.join([f'-replace={replacement}' for replacement in replace])}" if replace else '',
            'targets': f" {' '.join([f'-target={target}' for target in targets])}" if targets else '',
            'var_inputs': ''.join([f" -var '{v}'" for v in var_inputs]) if var_inputs else '',
            'compact_warnings': ' -compact-warnings' if compact_warnings else '',
            'detailed_exit_code': ' -detailed-exitcode' if detailed_exit_code else '',
            'input_false': ' -input=false' if input_false else '',
            'json': ' -json' if json else '',
            'lock_false': ' -lock=false' if lock_false else '',
        }

        self.command_string += ''.join(options_mapping.values())

        return self


    def apply(self):
        self.command_string += " apply"
        return self

    def add_variable(self, name, value):
        self.command_string += f' -var "{name}={value}"'
        return self

    def build(self):
        return TerraformCommand(self.command_string)
