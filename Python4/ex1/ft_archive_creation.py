import sys
import typing


def write_file(content: str) -> None:
    """
    write to the file taken from input
    with the content parsed from
    the read_file function and closes the file
    """
    fname = input("Enter new file name (or empty): ")
    if not fname:
        print("Not saving data.")
        return
    print(f"Saving data to \'{fname}\'")
    try:
        f = open(fname, "w+")
        f.write(content)
    except PermissionError:
        print(f"Error opening file \'{fname}\':"
              f" [Errno 13] Permission denied: \'{fname}\'")
        print("Data not saved")
        return
    print(f"Data saved in file \'{fname}\'.")
    f = open(fname, "w+")
    f.write(content)
    f.close()


def read_file(f: typing.IO[str]) -> str:
    """
    Reads the file given, prints the content, aswell as
    storing the file contents as content and returning
    content.
    """
    print("---\n")
    content: str = f.read()
    print(content)
    print("\n---")
    return content


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
        content = read_file(f)
        f.close()
        print(f"File \'{argv[1]}\' closed.\n")
        print("Transform data:\n---\n")
        new_content: str = ""
        for line in content.splitlines():
            new_content += line + "#\n"
        print(f"{new_content}\n---")
        write_file(new_content)
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
