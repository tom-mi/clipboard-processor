import signal
import time

import pytest
from test_cli import SLEEP_STARTUP_SECONDS, BASE64_DATA, SLEEP_PROCESSING_SECONDS_UI
from util import run_cli, copy_to_clipboard


@pytest.fixture(autouse=True)
def empty_clipboard():
    copy_to_clipboard('')


@pytest.mark.snapshot
def test_cli_with_ui_and_stdout(take_screenshot, image_snapshot, snapshot_path):
    # when
    with run_cli('-o', 'ui', '-o', 'stdout') as proc:
        time.sleep(SLEEP_STARTUP_SECONDS)
        copy_to_clipboard(BASE64_DATA)
        time.sleep(SLEEP_PROCESSING_SECONDS_UI)
        screenshot = take_screenshot()
        proc.send_signal(signal.SIGINT)

        output = proc.stdout.readlines()

    # then
    assert proc.returncode == 0
    assert BASE64_DATA in output[0]  # ensure clipboard has been processed, so we can expect an overlay

    image_snapshot(screenshot, snapshot_path, threshold=0.4)
