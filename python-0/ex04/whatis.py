import sys


def main():
    if len(sys.argv) < 2:
        return
    try:
        assert len(sys.argv) == 2, "more than one argument is provided"
        num = int(sys.argv[1])
        if (num % 2):
            print("I'm Odd")
        else:
            print("I'm Even")
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except ValueError:
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    main()
