from src.commands.command import Command
from src.builders.terraform_command_builder import TerraformCommandBuilder
from src.commands.terraform_command import TerraformCommand
from src.builders.command_runner import CommandRunner
import pytest

def test_terraform_command_execute():
    terraform_command = TerraformCommand("dummy_command")
    output = terraform_command.execute()
    assert output == "Executing Terraform command: dummy_command"

def test_build_terraform_command():
    builder = TerraformCommandBuilder()
    terraform_command = (
        builder
        .start_init()
        .add_variable("region", "us-west-1")
        .start_plan()
        .build()
    )
    assert isinstance(terraform_command, TerraformCommand)
    assert terraform_command.command_string == "terraform init -var \"region=us-west-1\" plan"

def test_command_runner_run_command():
    runner = CommandRunner()
    terraform_command = TerraformCommand("dummy_command")
    output = runner.run_command(terraform_command.command_string)
    assert output == "Executing command: dummy_command"
