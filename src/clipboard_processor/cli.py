import argparse
import sys
import time

from clipboard_processor.input import PyperclipInput, XclipPrimaryInput
from clipboard_processor.output import NotifyOutput
from clipboard_processor.plugins import *

INPUTS = [
    PyperclipInput,
    XclipPrimaryInput,
]

PLUGINS = [
    AwsAccountIdPlugin,
    Base64Plugin,
    JwtPlugin,
    UlidPlugin,
    UnixTimePlugin,
    VinPlugin,
]


def main():
    available_plugin_names = [p.name() for p in PLUGINS if p.is_available()]
    available_input_names = [i.name() for i in INPUTS if i.is_available()]

    if not available_plugin_names:
        print('No plugins available. Please check README and install dependencies if needed. Exiting.')
        sys.exit(1)

    if not available_input_names:
        print('No input methods available. Please check README and install dependencies if needed. Exiting.')
        sys.exit(1)

    parser = argparse.ArgumentParser(description='Automatic clipboard processor')
    plugin_group = parser.add_mutually_exclusive_group()
    plugin_group.add_argument('--all', action='store_true', help='Process all clipboard data', default=False)
    plugin_group.add_argument('-p', '--plugin', action='append',
                              help='Process clipboard data with specific plugin',
                              choices=available_plugin_names, default=[])
    parser.add_argument('--input', action='store', help='Select input method',
                        choices=available_input_names, default=available_input_names[0])
    args = parser.parse_args()

    active_plugins = []
    if args.all:
        active_plugins = [p() for p in PLUGINS]
    elif len(args.plugin) > 0:
        active_plugins = [p() for p in PLUGINS if p.name() in args.plugin]
    else:
        parser.error('No plugins specified. Exiting.')

    outputs = [NotifyOutput()]
    input_ = [i for i in INPUTS if i.name() == args.input][0]()

    last_value = None
    while True:
        try:
            current_value = input_.read()
            if last_value is None:
                last_value = current_value
            elif current_value != last_value:
                last_value = current_value
                results = []
                for plugin in active_plugins:
                    results.extend(plugin.process(current_value))

                if results:
                    title = _trim(current_value, max_length=50)
                    content = '\n'.join(results)
                    for output in outputs:
                        output.show(title, content)

            time.sleep(0.1)
        except KeyboardInterrupt:
            break


def _trim(s: str, max_length: int) -> str:
    return s[:max_length] + ('...' if len(s) > max_length else '')
