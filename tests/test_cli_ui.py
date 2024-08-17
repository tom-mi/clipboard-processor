import signal
import time

import pytest

from test_cli import SLEEP_STARTUP_SECONDS, SLEEP_PROCESSING_SECONDS, VIN, BASE64_DECODED, BASE64_DATA
from util import run_cli, copy_to_clipboard


@pytest.fixture(autouse=True)
def empty_clipboard():
    copy_to_clipboard('')


@pytest.mark.snapshot
def test_cli_without_arguments(take_screenshot, image_snapshot, snapshot_path):
    # when
    with run_cli() as proc:
        time.sleep(SLEEP_STARTUP_SECONDS)
        copy_to_clipboard(VIN)
        time.sleep(SLEEP_PROCESSING_SECONDS)
        screenshot = take_screenshot()
        proc.send_signal(signal.SIGINT)

    # then
    assert proc.returncode == 0
    image_snapshot(screenshot, snapshot_path)
