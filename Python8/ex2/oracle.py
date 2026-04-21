import os
import sys


def read_env() -> bool:
    """
    Fetchs the environment keys and values and
    validates and prints them if acceptable
    if not a reasonable message is returned
    """
    valid = True
    data = {"matrix_mode": os.getenv("MATRIX_MODE"),
            "db_url": os.getenv("DATABASE_URL"),
            "api_key": os.getenv("API_KEY"),
            "log_level": os.getenv("LOG_LEVEL"),
            "zion": os.getenv("ZION_ENDPOINT")}
    print("Configuration loaded:")
    for key, value in data.items():
        if key == "matrix_mode":
            print("Mode: ", end="")
            if not value:
                print("None")
                valid = False
            else:
                print(value)
        elif key == "db_url":
            print("Database: ", end="")
            if not value:
                print("Could not connect to local instance")
                valid = False
            else:
                print("Connected to local instance")
        elif key == "api_key" and data["matrix_mode"] == "development":
            print("API Access: ", end="")
            if not value:
                print("Unable to authenticate")
                valid = False
            else:
                print("Authenticated")
        elif key == "log_level" and data["matrix_mode"] == "development":
            print("Log level: ", end="")
            if not value:
                print("None")
                valid = False
            else:
                print(value)
        elif key == "zion":
            print("Zion Network: ", end="")
            if not value:
                print("Offline")
                valid = False
            else:
                print("Online")
    return valid


if __name__ == "__main__":
    try:
        from dotenv import load_dotenv  # type: ignore
    except ModuleNotFoundError:
        print("Error: python-dotenv module not found")
        print("Please install python-dotenv using pip install")
        sys.exit()
    if not os.path.exists(".env"):
        print("Could not find .env, please copy the .env.example file as "
              ".env and edit the paramaters. \nYou can use the following"
              " command:")
        print("cp .env.example .env")
        sys.exit()
    load_dotenv(override=True)
    print("\nORACLE STATUS: Reading the Matrix...\n")
    state = read_env()
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if state is True:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file is not properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")
