import pytest


@pytest.fixture()
def setup():
    print("before test method3")
    yield
    print("after test method4py")
def testmethod1(setup):
    print("method3")
def testmethode(setup):
    print("method4")