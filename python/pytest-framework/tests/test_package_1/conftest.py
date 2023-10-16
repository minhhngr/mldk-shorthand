import pytest


@pytest.fixture(scope="package", autouse=True)
def setup_and_teardown():
    print("setup autouse")
    yield
    print("teardown autouse")


@pytest.fixture(scope="package")
def setup_and_teardown():
    print("setup not autouse")
    yield
    print("teardown not autouse")
