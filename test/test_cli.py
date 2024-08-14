import signal
import time

from util import run_cli, copy_to_clipboard

BASE64_DATA = 'dGVzdA=='
BASE64_DECODED = 'test'


def test_cli_without_arguments():
    # given
    copy_to_clipboard('')

    # when
    with run_cli() as proc:
        time.sleep(0.5)
        copy_to_clipboard(BASE64_DATA)
        time.sleep(0.1)
        proc.send_signal(signal.SIGINT)

        output = proc.stdout.readlines()

    # then
    assert proc.returncode == 0
    assert BASE64_DATA in output[0]
    assert output[1].strip() == BASE64_DECODED


def test_cli_with_plugin_matching_input():
    # given
    copy_to_clipboard('')

    # when
    with run_cli('--plugin', 'base64') as proc:
        time.sleep(0.5)
        copy_to_clipboard(BASE64_DATA)
        time.sleep(0.1)
        proc.send_signal(signal.SIGINT)

        output = proc.stdout.readlines()

    # then
    assert proc.returncode == 0
    assert BASE64_DATA in output[0]
    assert output[1].strip() == BASE64_DECODED


def test_cli_with_plugin_argument_not_matching_input():
    # given
    copy_to_clipboard('')

    # when
    with run_cli('--plugin', 'unixtime') as proc:
        time.sleep(0.5)
        copy_to_clipboard(BASE64_DATA)
        time.sleep(0.1)
        proc.send_signal(signal.SIGINT)

        output = proc.stdout.readlines()

    # then
    assert proc.returncode == 0
    assert len(output) == 0
