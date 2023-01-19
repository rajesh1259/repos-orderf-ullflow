import pytest

@pytest.fixture()
def setup():
    print("open url")
    yield
    print("close url")

def testemailsignup(setup):
    print("sign up by email")
def testfacebooksignup(setup):
    print("sign by facebook")
