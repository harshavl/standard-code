

#
#Description: How to write test case for commamd line interface
#

from hello import logic
from click.testing import CliRunner
from hello import harsha


def test_logic():
    assert "vardhana" in logic("harsha")
    assert 'No Match' in logic("test")


def test_harsha_argument():
    runner = CliRunner()
    result = runner.invoke( harsha, ['--name', 'harsha' ] )
    assert result.exit_code == 0
    assert 'vardhana' in result.output


def test_no_match_argument():
    runner = CliRunner()
    result = runner.invoke( harsha, ['--name', 'amoghavarsha' ] )
    assert result.exit_code == 0
    assert 'No Match' in result.output

