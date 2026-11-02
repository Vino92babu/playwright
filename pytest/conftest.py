import pytest


@pytest.fixture(scope="session")
def prework1():
    print("fix_2")
