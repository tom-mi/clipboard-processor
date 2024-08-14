from clipboard_processor.plugins import JwtPlugin

VALID_JWT = ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dnZWRJbk FzIjoiYWRtaW4iLCJpYXQiOjE0MjI3Nzk2Mzh9.'
             'gzSraSYS8EXBxLN _oWnFSRgCzcmJmMjLiuyu5CSpyHI=')


def test_valid_jwt():
    plugin = JwtPlugin()
    assert plugin.process(VALID_JWT) == ['{\n  "loggedInAs": "admin",\n  "iat": 1422779638\n}']


def test_valid_jwt_with_bearer():
    plugin = JwtPlugin()
    assert plugin.process('Bearer ' + VALID_JWT) == ['{\n  "loggedInAs": "admin",\n  "iat": 1422779638\n}']


def test_invalid_jwt():
    plugin = JwtPlugin()
    assert plugin.process(VALID_JWT[0:20]) == []
