import sys
import typing


def read_file(f: typing.IO[str]) -> None:
    """
    Reads the file given, prints the content and
    then closes the file
    """
    print("---\n")
    print(f.read())
    print("\n---")


def open_file() -> None:
    """
    Checks that the argument given is valid
    """
    argv = sys.argv
    print("=== Cyber Archives Recovery ===")
    try:
        if len(argv) == 1:
            raise FileNotFoundError("Usage: ft_ancient_text.py <file>")
        elif len(argv) > 2:
            raise ValueError("Error: Too many files were provided")
    except (FileNotFoundError, ValueError) as message:
        print(f"{message}\n")
        return
    try:
        print(f"Accessing file \'{argv[1]}\'")
        f = open(argv[1])
        read_file(f)
        f.close()
        print(f"File \'{argv[1]}\' closed.")
    except FileNotFoundError:
        print(f"Error opening file \'{argv[1]}\':"
              f" [Errno2] No such file or firectoy: \'{argv[1]}\'")
    except PermissionError:
        print(f"Error opening file \'{argv[1]}\':"
              f" [Errno 13] Permission denied: \'{argv[1]}\'")
    finally:
        print()


if __name__ == "__main__":
    open_file()
