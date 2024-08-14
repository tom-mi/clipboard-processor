# clipboard-processor

Process clipboard content and show helpful notifications based on the content,
e.g. parse UNIX timestamps, AWS account IDs, VINs, base64 strings and more.

All parsing & decoding is done locally. The clipboard content is not sent to any external service.

## Installation

## Usage

## Functionality

### Input

This tool uses [pyperclip](https://github.com/asweigart/pyperclip) for cross-platform clipboard access.
Whenever the clipboard content changes, the content is passed to the plugins for processing.

On linux, you can also use the input mode `xclip-primary` to use the primary selection instead of the clipboard,
which makes the tool more convenient to use.

### Plugins

All decoding functionality is provided via plugins.

| Plugin           | Description                                                                                                 | External library                                     |
|------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| `aws_account_id` | Show AWS account name for given AWS account ID by parsing `~/.aws/config`                                   | -                                                    |
| `base64`         | Decode base64 strings                                                                                       | -                                                    |
| `jwt`            | Decode JSON web tokens (JWTs)                                                                               | [PyJWT](https://github.com/jpadilla/pyjwt)           |
| `ulid`           | Parse [ULIDs](https://github.com/ulid/spec) and show the encoded timestamp                                  | [python-ulid](https://github.com/mdomke/python-ulid) |
| `unixtime`       | Parse UNIX timestamps and show the human-readable (ISO 8601) time                                           | -                                                    |
| `vin`            | Decode [Vehicle Identification Numbers](https://en.wikipedia.org/wiki/Vehicle_identification_number) (VINs) | [vininfo](https://github.com/idlesign/vininfo)       |

### Output

This tool uses [desktop-notifier](https://github.com/SamSchott/desktop-notifier) to show the result of the processing
via cross-platform desktop notifications.
