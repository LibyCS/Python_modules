import sys
import typing


def write_file(content: str) -> None:
    """
    write to the file taken from input
    with the content parsed from
    the read_file function and closes the file
    """
    print("Enter new file name (or empty): ", end="", flush=True,
          file=sys.stdout)
    fname = sys.stdin.readline().strip('\n')
    if not fname:
        print("Not saving data.")
        return
    print(f"Saving data to \'{fname}\'", file=sys.stdout)
    try:
        f = open(fname, "w+")
        f.write(content)
    except PermissionError:
        print(f"[STDERR] Error opening file \'{fname}\':"
              f" [Errno 13] Permission denied: \'{fname}\'",
              file=sys.stderr)
        print("Data not saved", file=sys.stdout)
        return
    finally:
        f.close()
    print(f"Data saved in file \'{fname}\'.", file=sys.stdout)


def read_file(f: typing.IO[str]) -> str:
    """
    Reads the file given, prints the content, aswell as
    storing the file contents as content and returning
    content.
    """
    print("---\n", file=sys.stdout)
    content: str = f.read()
    print(content, file=sys.stdout)
    print("\n---", file=sys.stdout)
    return content


def open_file() -> None:
    """
    Checks that the argument given is valid
    """
    argv = sys.argv
    print("=== Cyber Archives Recovery & Preservation ===", file=sys.stdout)
    try:
        if len(argv) == 1:
            raise FileNotFoundError("Usage: ft_ancient_text.py <file>")
        elif len(argv) > 2:
            raise ValueError("Error: Too many files were provided")
    except (FileNotFoundError, ValueError) as message:
        print(f"[STDERR] {message}\n", file=sys.stderr)
        return
    try:
        print(f"Accessing file \'{argv[1]}\'", file=sys.stdout)
        f = open(argv[1])
        content = read_file(f)
        f.close()
        print(f"File \'{argv[1]}\' closed.\n", file=sys.stdout)
        print("Transform data:\n---\n", file=sys.stdout)
        new_content: str = ""
        for line in content.splitlines():
            new_content += line + "#\n"
        print(f"{new_content}\n---", file=sys.stdout)
        write_file(new_content)
    except FileNotFoundError:
        print(f"[STDERR] Error opening file \'{argv[1]}\':"
              f" [Errno2] No such file or firectoy: \'{argv[1]}\'",
              file=sys.stderr)
    except PermissionError:
        print(f"[STDERR] Error opening file \'{argv[1]}\':"
              f" [Errno 13] Permission denied: \'{argv[1]}\'",
              file=sys.stderr)
    finally:
        print("", file=sys.stdout)


if __name__ == "__main__":
    open_file()
