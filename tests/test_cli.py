import signal
import time

import pytest

from util import run_cli, copy_to_clipboard

BASE64_DATA = 'dGVzdA=='
BASE64_DECODED = 'test'

VIN = 'JF2SHADC3DG417185'
VIN_CONTENT = 'Manufacturer: Subaru'

SLEEP_STARTUP_SECONDS = 0.5
SLEEP_PROCESSING_SECONDS = 0.2
SLEEP_PROCESSING_SECONDS_UI = 2


@pytest.fixture(autouse=True)
def empty_clipboard():
    copy_to_clipboard('')


def test_cli_with_default_plugins():
    # when
    with run_cli('--output', 'stdout') as proc:
        time.sleep(SLEEP_STARTUP_SECONDS)
        copy_to_clipboard(BASE64_DATA)
        time.sleep(SLEEP_PROCESSING_SECONDS)
        proc.send_signal(signal.SIGINT)

        output = proc.stdout.readlines()

    # then
    assert proc.returncode == 0
    assert BASE64_DATA in output[0]
    assert output[1].strip() == BASE64_DECODED


def test_cli_with_plugin_matching_input():
    # when
    with run_cli('--plugin', 'base64', '--output', 'stdout') as proc:
        time.sleep(SLEEP_STARTUP_SECONDS)
        copy_to_clipboard(BASE64_DATA)
        time.sleep(SLEEP_PROCESSING_SECONDS)
        proc.send_signal(signal.SIGINT)

        output = proc.stdout.readlines()

    # then
    assert proc.returncode == 0
    assert BASE64_DATA in output[0]
    assert output[1].strip() == BASE64_DECODED


def test_cli_with_plugin_argument_not_matching_input():
    # when
    with run_cli('--plugin', 'unixtime', '--output', 'stdout') as proc:
        time.sleep(SLEEP_STARTUP_SECONDS)
        copy_to_clipboard(BASE64_DATA)
        time.sleep(SLEEP_PROCESSING_SECONDS)
        proc.send_signal(signal.SIGINT)

        output = proc.stdout.readlines()

    # then
    assert proc.returncode == 0
    assert len(output) == 0


@pytest.mark.full_installation
def test_cli_with_optional_feature_available():
    # when
    with run_cli('--output', 'stdout') as proc:
        time.sleep(SLEEP_STARTUP_SECONDS)
        copy_to_clipboard(VIN)
        time.sleep(SLEEP_PROCESSING_SECONDS)
        proc.send_signal(signal.SIGINT)

        output = proc.stdout.readlines()

    # then
    assert proc.returncode == 0
    assert VIN in output[0]
    assert VIN_CONTENT in [s.strip() for s in output[1:]]


@pytest.mark.minimal_installation
def test_cli_with_optional_feature_not_available():
    # when
    with run_cli('--output', 'stdout') as proc:
        time.sleep(SLEEP_STARTUP_SECONDS)
        copy_to_clipboard(VIN)
        time.sleep(SLEEP_PROCESSING_SECONDS)
        proc.send_signal(signal.SIGINT)

        output = proc.stdout.readlines()

    # then
    assert proc.returncode == 0
    assert len(output) == 0
