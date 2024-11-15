from ml_boilerplate.main import hello_numpy, hello_torch, hello_world


def test_hello_world() -> None:
    assert hello_world() == "Hello World"


def test_hello_numpy() -> None:
    assert hello_numpy() == "Hello Numpy"


def test_hello_torch() -> None:
    assert hello_torch() == "Hello PyTorch"
