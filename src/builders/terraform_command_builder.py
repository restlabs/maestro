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
             lock_false: bool = None,
             no_color: bool = None
             ) -> str:

        self.command_string += " plan"

        command_options = self.terraform_command_options(var_file_name, plan_output_file_name, destroy, refresh_only,
                                                         refresh_false, replace, targets, var_inputs, compact_warnings,
                                                         detailed_exit_code, input_false, json, lock_false, no_color)

        self.command_string += ''.join(command_options.values())

        return self

    def apply(
            self,
            var_inputs: list[str] = None,
            auto_approve: bool = None,
            compact_warnings: bool = None,
    ) -> str:

        self.command_string += " apply"

        options_mapping = {
            'var_inputs': ''.join([f" -var '{v}'" for v in var_inputs]) if var_inputs else '',
            'auto_approve': ' -auto-approve' if auto_approve else '',
            'compact_warnings': ' -compact-warnings' if compact_warnings else '',
        }

        self.command_string += ''.join(options_mapping.values())

        return self

    def build(self):
        return TerraformCommand(self.command_string)

    def terraform_command_options(self, var_file_name=None, plan_output_file_name=None, destroy=False,
                                  refresh_only=False, refresh_false=False, replace=None,
                                  targets=None, var_inputs=None, compact_warnings=False,
                                  detailed_exit_code=False, input_false=False, json=False,
                                  lock_false=False, no_color=False):
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
            'no_color': ' -no-color' if no_color else ''
        }

        command_options = {key: value for key,
                           value in options_mapping.items() if value}
        return command_options
