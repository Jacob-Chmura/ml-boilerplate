from ml_boilerplate.main import hello_world, hello_numpy


def test_hello_world() -> None:
    assert hello_world() == "Hello World"


def test_hello_numpy() -> None:
    assert hello_numpy() == "Hello Numpy"
