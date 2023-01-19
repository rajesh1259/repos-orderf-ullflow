import pytest

@pytest.fixture()
def setup():
    print("before every method")

def testmethod1(setup):
    print("methd1")
def testmethod2(setup):
    print("method2")