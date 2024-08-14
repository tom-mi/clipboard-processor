from clipboard_processor.plugins import VinPlugin


def test_valid_vin():
    plugin = VinPlugin()
    assert plugin.process('JF2SHADC3DG417185') == ['Country: Japan', 'Manufacturer: Subaru', 'Region: Asia',
                                                   'Years: 2013, 1983']
    assert plugin.process('JF2SHADC3DG417000') == ['Country: Japan', 'Manufacturer: Subaru', 'Region: Asia',
                                                   'Years: 2013, 1983', 'Checksum invalid!']


def test_invalid_vin():
    plugin = VinPlugin()
    assert plugin.process('JF2SHADC3DG417') == []
