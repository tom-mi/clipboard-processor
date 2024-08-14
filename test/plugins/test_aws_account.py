import pytest

from clipboard_processor.plugins import AwsAccountIdPlugin


@pytest.fixture
def aws_config(tmp_path):
    config = tmp_path / 'config'
    config.write_text("""
    [profile my-test-account-profile]
    sso_account_id = 123456789012
    sso_account_name = test-account
    """)
    return config


@pytest.fixture
def mock_config_path(aws_config, monkeypatch):
    monkeypatch.setattr('clipboard_processor.plugins.aws_account_id._CONFIG_FILE', aws_config)


def test_valid_account_id(mock_config_path):
    plugin = AwsAccountIdPlugin()
    assert plugin.process('123456789012') == ['test-account']


def test_unknown_account_id(mock_config_path):
    plugin = AwsAccountIdPlugin()
    assert plugin.process('987654321098') == []
