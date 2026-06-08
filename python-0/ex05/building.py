import sys


def main():
    '''Analyzes a given text or standard input and counts its character types.

    The function counts uppercase letters, lowercase letters, \
        punctuation marks,
    spaces (including carriage returns), and digits. It accepts text\
        either
    as a single command-line argument or from standard input (sys.stdin).

    Raises:
        AssertionError: If more than one command-line argument is provided. '''
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) < 2:
            print("What is the text to count?")
            line = sys.stdin.read()
        else:
            line = sys.argv[1]
        lower = 0
        upper = 0
        puntuaction_marks = 0
        spaces = 0
        digits = 0
        punctuation_set = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        for i in line:
            if (i.islower()):
                lower += 1
            elif (i.isupper()):
                upper += 1
            elif (i.isdigit()):
                digits += 1
            elif (i.isspace()):
                spaces += 1
            elif i in punctuation_set:
                puntuaction_marks += 1
        print(f"The text contains {len(line)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{puntuaction_marks} puntuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")


if __name__ == "__main__":
    main()
