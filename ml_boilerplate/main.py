def hello_world() -> str:
    return "Hello World"


def hello_numpy() -> str:
    import numpy as np

    _ = np.zeros(1337)
    return "Hello Numpy"


def main() -> None:
    print("Checking packages...", end="")
    hello_world()
    hello_numpy()
    print("Ok.")


if __name__ == "__main__":
    main()
