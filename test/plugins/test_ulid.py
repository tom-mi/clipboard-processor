from clipboard_processor.plugins import UlidPlugin


def test_valid_ulid():
    plugin = UlidPlugin()
    assert plugin.process('01ARZ3NDEKTSV4RRFFQ69G5FAV') == ['ULID at 2016-07-30 23:54:10.259000Z']


def test_invalid_ulid():
    plugin = UlidPlugin()
    assert plugin.process('01ARZ3NDEKTSV4RRFFQ69G5FAv') == []
