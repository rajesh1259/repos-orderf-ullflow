import pytest

@pytest.fixture()
def setup():
    print("open url")
    yield
    print("close url")

def testemaillogin(setup):
    print("login by email")
def testfacebooklogin(setup):
    print("login by facebook")
