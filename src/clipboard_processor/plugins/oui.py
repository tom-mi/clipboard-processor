import re

from clipboard_processor.plugins._base import Plugin

try:
    import netaddr
except ImportError:
    netaddr = None

_REGEX = re.compile(r'([0-9A-Fa-f]{2}[:-]?){2,5}([0-9A-Fa-f]{2})')


class OuiPlugin(Plugin):

    @classmethod
    def name(cls) -> str:
        return 'oui'

    @classmethod
    def is_available(cls) -> bool:
        return netaddr is not None

    def process(self, data: str) -> [str]:
        results = []
        if _REGEX.match(data):
            if len(data) == 17:
                data = data[0:8]
            elif len(data) == 12:
                data = data[0:6]
            try:
                oui = netaddr.OUI(data.replace(':', '-'))
                results.append(f'{oui.registration().org} ({oui})')
            except netaddr.core.NotRegisteredError:
                pass
        return results
