from llm.plugins import pm
from click.testing import CliRunner
from llm_cmd import register_commands


def test_plugin_is_installed():
    names = [mod.__name__ for mod in pm.get_plugins()]
    assert "llm_cmd" in names

def test_print_only_flag():
    runner = CliRunner()
    
    result = runner.invoke(cmd, ["--print-only", "list files"])
    assert result.exit_code == 0
    # Should output just the command without any prefix
    assert result.output.strip() == "ls"


def test_no_print_flag():
    runner = CliRunner()
    
    result = runner.invoke(cmd, ["list files"])
    assert result.exit_code == 0
    # Should not contain the command output directly
    assert "ls" not in result.output
