def hello_world() -> str:
    return "Hello World"


def main() -> None:
    print("Checking packages...", end="")
    hello_world()
    print("Ok.")


if __name__ == "__main__":
    main()
