from clipboard_processor.output._base import Output


class NotifyOutput(Output):

    def __init__(self):
        super().__init__()
        from desktop_notifier.sync import DesktopNotifierSync
        self._notifier = DesktopNotifierSync(app_name='clipboard-processor', app_icon=None)

    @classmethod
    def name(cls):
        return 'notify'

    @classmethod
    def is_available(cls):
        try:
            from desktop_notifier.sync import DesktopNotifierSync
            return True
        except ImportError:
            return False

    def show(self, title: str, content: str):
        self._notifier.send(title, content)
