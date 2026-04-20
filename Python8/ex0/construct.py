import sys
import os
import site


def python_info(state: bool) -> None:
    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: ", end="")
    if state is False:
        print("None detected")
    else:
        print(os.path.basename(sys.prefix))
        print(f"Environment Path: {sys.prefix}")


if __name__ == "__main__":
    print("\nMATRIX STATUS: ", end="")
    if sys.prefix == sys.base_prefix:
        print("You're still plugged in")
        python_info(False)
        print("\nWARNING: You're in the global environment!"
              "\nThe machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("Unix: source matrix_env/bin/activate")
        print(r"Windows: matrix_env\Scripts\activate")
        print("\nThen run this program again.")
    else:
        print("Welcome to the construct")
        python_info(True)
        print("\nSUCCESS: You're in an isolated environment!"
              "\nSafe to install packages without affecting"
              "\nthe global system.")
        print("\nPackage installation path:")
        for path in site.getsitepackages():
            if "site-packages" in path and sys.prefix in path:
                print(path)
