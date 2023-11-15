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

    def plan(self, **kwargs) -> str:
        command_mapping = {
            'var_file_name': lambda file_value: f' -var-file={file_value}',
            'plan_output_file_name': lambda output_value: f' -out={output_value}',
            'destroy': lambda destroy_value: ' -destroy',
            'refresh_only': lambda refresh_value: ' -refresh-only',
            'refresh_false': lambda refresh_false_value: ' -refresh=false',
            'replace': lambda replacements: ''.join([f' -replace={replacement}' for replacement in replacements]),
            'targets': lambda target_values: ''.join([f' -target={target}' for target in target_values]),
            'var_inputs': lambda var_values: ''.join([f" -var '{var}'" for var in var_values]),
            'compact_warnings': lambda compact_warnings_value: ' -compact-warnings',
            'detailed_exit_code': lambda detailed_exit_code_value: ' -detailed-exitcode',
            'input_false': lambda input_false_value: ' -input=false',
            'json': lambda json_value: ' -json',
        }

        self.command_string += ' plan'

        for arg, value in kwargs.items():
            if arg in command_mapping:
                self.command_string += command_mapping[arg](value)

        return self



    def apply(self):
        self.command_string += " apply"
        return self

    def add_variable(self, name, value):
        self.command_string += f' -var "{name}={value}"'
        return self

    def build(self):
        return TerraformCommand(self.command_string)
