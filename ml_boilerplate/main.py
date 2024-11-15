def hello_world() -> str:
    return "Hello World"


def hello_numpy() -> str:
    import numpy as np

    _ = np.zeros(1337)
    return "Hello Numpy"


def hello_torch() -> str:
    import torch

    _ = torch.zeros(1337)
    return "Hello PyTorch"


def main() -> None:
    print("Checking packages...", end="")
    hello_world()
    hello_numpy()
    hello_torch()
    print("Ok.")


if __name__ == "__main__":
    main()
