def secure_archive(fname: str, perms: str = 'r', content: str = ""
                   ) -> tuple[bool, str]:
    try:
        if perms != 'r' and perms != 'w':
            raise ValueError
        with open(fname, perms) as f:
            if perms == 'r':
                file_content = f.read()
            elif perms == 'w' and content:
                f.write(content)
                file_content = content
            return (True, file_content)
    except FileNotFoundError:
        return (False, "[Errno 2] No such file or directory:"
                f" \'{fname}\'")
    except PermissionError:
        return (False, "[Errno 13] Permission denied:"
                f" \'{fname}\'")
    except ValueError:
        return (False, "File action must be \'r\' or \'w\'.")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("./etc/master.passwd"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w",
                         "Content successfully written to file"))
