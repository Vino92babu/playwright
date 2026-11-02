import pytest

@pytest.fixture(scope="function")
def prework():
    print("fix_1")

def test_demo1(prework):
    print("This is demo 1")

def test_demo2(prework1):
    print("This is demo 2")
