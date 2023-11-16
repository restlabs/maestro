from src.commands.command import Command
from src.builders.terraform_command_builder import TerraformCommandBuilder
from src.commands.terraform_command import TerraformCommand
from src.commands.command_runner import CommandRunner
import pytest

def test_terraform_command_execute():
    terraform_command = TerraformCommand("dummy_command")
    output = terraform_command.execute()
    assert output == "dummy_command"

def test_build_terraform_init_command():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .init()
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform init"

def test_build_terraform_init_reconfigure_command():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .init(
            backend_config="test"
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform init -reconfigure -backend-config=test"

def test_build_terraform_plan_command():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan()
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan"

def test_build_terraform_plan_command_with_var_file():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            var_file_name="test"
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -var-file=test"

def test_build_terraform_plan_command_with_plan_output():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            plan_output_file_name="test"
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -out=test"

def test_build_terraform_plan_command_with_destroy():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            destroy=True
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -destroy"

def test_build_terraform_plan_command_with_refresh():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            refresh_only=True
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -refresh-only"

def test_build_terraform_plan_command_with_var_file_destroy():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            var_file_name="test",
            destroy=True
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -var-file=test -destroy"

def test_build_terraform_plan_command_with_refresh_false():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            refresh_false=True
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -refresh=false"

def test_build_terraform_plan_command_with_multiple_replace():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            replace=["test","test2"]
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -replace=test -replace=test2"

def test_build_terraform_plan_command_with_multiple_target():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            targets=["test","test2"]
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -target=test -target=test2"

def test_build_terraform_plan_command_with_var_input():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            var_inputs=["KEY=VALUE"]
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -var 'KEY=VALUE'"

def test_build_terraform_plan_command_with_var_inputs():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            var_inputs=["KEY=VALUE","KEY2=VALUE2", "KEY3=VALUE3"]
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -var 'KEY=VALUE' -var 'KEY2=VALUE2' -var 'KEY3=VALUE3'"

def test_build_terraform_plan_command_with_compact_warnings():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            compact_warnings=True
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -compact-warnings"

def test_build_terraform_plan_command_with_detailed_exit_code():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            detailed_exit_code=True
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -detailed-exitcode"

def test_build_terraform_plan_command_with_input_false():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            input_false=True
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -input=false"

def test_build_terraform_plan_command_with_json():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            json=True
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -json"

def test_build_terraform_plan_command_with_lock_false():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            lock_false=True
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -lock=false"

def test_build_terraform_plan_command_with_no_color():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan(
            no_color=True
        )
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan -no-color"

def test_build_terraform_apply_with_variables_command():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .apply()
        .add_variable("region", "us-west-1")
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform apply -var \"region=us-west-1\""

def test_command_runner_run_command():
    runner = CommandRunner()
    terraform_command = TerraformCommand("dummy_command")
    output = runner.run_command(terraform_command.execute())
    assert output == "Executing command: dummy_command"
