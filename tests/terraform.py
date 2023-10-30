from src.commands.command import Command
from src.builders.terraform_command_builder import TerraformCommandBuilder
from src.commands.terraform_command import TerraformCommand
from src.builders.command_runner import CommandRunner
import pytest

def test_terraform_command_execute():
    terraform_command = TerraformCommand("dummy_command")
    output = terraform_command.execute()
    assert output == "Executing Terraform command: dummy_command"

def test_build_terraform_init_command():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .init()
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform init"

def test_build_terraform_plan_command():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .plan()
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform plan"


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
    output = runner.run_command(terraform_command.command_string)
    assert output == "Executing command: dummy_command"
