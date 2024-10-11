from clipboard_processor.plugins._base import Plugin

try:
    import cron_descriptor
except ImportError:
    cron_descriptor = None


class CronPlugin(Plugin):

    @classmethod
    def name(cls) -> str:
        return 'cron'

    @classmethod
    def is_available(cls) -> bool:
        return cron_descriptor is not None

    def process(self, data: str) -> [str]:
        results = []
        try:
            cron = str(cron_descriptor.ExpressionDescriptor(expression=data, use_24hour_time_format=True))
            results.append(cron)
        except cron_descriptor.Exception.FormatException:
            pass
        return results
