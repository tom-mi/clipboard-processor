from clipboard_processor.output._base import Output

from desktop_notifier.sync import DesktopNotifierSync


class NotifyOutput(Output):

    def __init__(self):
        super().__init__()
        self._notifier = DesktopNotifierSync(app_name='clipboard-processor', app_icon=None)

    def show(self, title: str, content: str):
        self._notifier.send(title, content)
