import sys
import importlib.util as util
import importlib.metadata as md


def comparison() -> bool:
    failed: bool = False
    if util.find_spec("pandas"):
        print(f"[OK] pandas ({md.version("pandas")}) "
              "- Data manipulation ready")
    else:
        print("[ERROR] Missing dependency pandas")
        failed = True
    if util.find_spec("numpy"):
        print(f"[OK] numpy ({md.version("numpy")}) "
              "- Numerical computation ready")
    else:
        print("[ERROR] Missing dependency numpy")
        failed = True
    if util.find_spec("matplotlib"):
        print(f"[OK] matplotlib ({md.version("matplotlib")}) "
              "- Visualisation ready")
    else:
        print("[ERROR] Missing dependency matplotlib")
        failed = True
    return failed


def analysis() -> None:
    print("\nAnalysing Matrix data...")
    data = np.random.randint(100, size=(1000, 2))
    data = data + 10
    print("Processing 1000 data points...")
    data_table = pd.DataFrame(data, columns=["x", "y"])
    print("Genertating visualisation...")
    plt.scatter(data_table["x"], data_table["y"])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Matrix Data")
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    if comparison() is True:
        print("\nTo install via pip please run the following commands")
        print("pip install -r requirements.txt")
        print("python3 loading.py")
        print("\nTo install via poetry please run the following commands")
        print("poetry install")
        print("poetry run python loading.py")
        sys.exit()
    import pandas as pd  # type: ignore
    import numpy as np  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
    analysis()
