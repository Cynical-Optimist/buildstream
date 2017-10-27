import os
import pytest
from buildstream import _yaml
from buildstream import LoadError, LoadErrorReason
from tests.testutils.runcli import cli

# Project directory
DATA_DIR = os.path.dirname(os.path.realpath(__file__))


@pytest.mark.datafiles(DATA_DIR)
@pytest.mark.parametrize("target,option,value,expected", [
    # Test 'var == "foo"' syntax
    ('element.bst', 'brother', 'pony', 'a pony'),
    ('element.bst', 'brother', 'zebry', 'a zebry'),
    ('element.bst', 'brother', 'horsy', 'a horsy'),
    # Test 'var1 == var2' syntax
    ('element-compare.bst', 'brother', 'horsy', 'different'),
    ('element-compare.bst', 'brother', 'zebry', 'same'),
    ('element-compare.bst', 'sister', 'pony', 'same'),
])
def test_conditional_cli(cli, datafiles, target, option, value, expected):
    project = os.path.join(datafiles.dirname, datafiles.basename, 'option-enum')
    result = cli.run(project=project, silent=True, args=[
        '--option', option, value,
        'show',
        '--deps', 'none',
        '--format', '%{vars}',
        target])

    assert result.exit_code == 0
    loaded = _yaml.load_data(result.output)
    assert loaded['result'] == expected


@pytest.mark.datafiles(DATA_DIR)
@pytest.mark.parametrize("target,option,value,expected", [
    # Test 'var == "foo"' syntax
    ('element.bst', 'brother', 'pony', 'a pony'),
    ('element.bst', 'brother', 'zebry', 'a zebry'),
    ('element.bst', 'brother', 'horsy', 'a horsy'),
    # Test 'var1 == var2' syntax
    ('element-compare.bst', 'brother', 'horsy', 'different'),
    ('element-compare.bst', 'brother', 'zebry', 'same'),
    ('element-compare.bst', 'sister', 'pony', 'same'),
])
def test_conditional_config(cli, datafiles, target, option, value, expected):
    project = os.path.join(datafiles.dirname, datafiles.basename, 'option-enum')
    cli.configure({
        'projects': {
            'test': {
                'options': {
                    option: value
                }
            }
        }
    })
    result = cli.run(project=project, silent=True, args=[
        'show',
        '--deps', 'none',
        '--format', '%{vars}',
        target])

    assert result.exit_code == 0
    loaded = _yaml.load_data(result.output)
    assert loaded['result'] == expected


@pytest.mark.datafiles(DATA_DIR)
def test_invalid_value_cli(cli, datafiles):
    project = os.path.join(datafiles.dirname, datafiles.basename, 'option-enum')
    result = cli.run(project=project, silent=True, args=[
        '--option', 'brother', 'giraffy',
        'show',
        '--deps', 'none',
        '--format', '%{vars}',
        'element.bst'])
    assert result.exit_code != 0
    assert result.exception
    assert isinstance(result.exception, LoadError)
    assert result.exception.reason == LoadErrorReason.INVALID_DATA


@pytest.mark.datafiles(DATA_DIR)
@pytest.mark.parametrize("config_option", [
    ('giraffy'), (['its', 'a', 'list']), ({'dic': 'tionary'})
])
def test_invalid_value_config(cli, datafiles, config_option):
    project = os.path.join(datafiles.dirname, datafiles.basename, 'option-enum')
    cli.configure({
        'projects': {
            'test': {
                'options': {
                    'brother': config_option
                }
            }
        }
    })
    result = cli.run(project=project, silent=True, args=[
        'show',
        '--deps', 'none',
        '--format', '%{vars}',
        'element.bst'])
    assert result.exit_code != 0
    assert result.exception
    assert isinstance(result.exception, LoadError)
    assert result.exception.reason == LoadErrorReason.INVALID_DATA


@pytest.mark.datafiles(DATA_DIR)
def test_missing_values(cli, datafiles):
    project = os.path.join(datafiles.dirname, datafiles.basename, 'option-enum-missing')
    result = cli.run(project=project, silent=True, args=[
        'show',
        '--deps', 'none',
        '--format', '%{vars}',
        'element.bst'])
    assert result.exit_code != 0
    assert result.exception
    assert isinstance(result.exception, LoadError)
    assert result.exception.reason == LoadErrorReason.INVALID_DATA