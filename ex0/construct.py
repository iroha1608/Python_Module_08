import sys
import os
import site


def check_matrix_status() -> None:
    is_venv = sys.prefix != sys.base_prefix

    if not is_venv:
        vir_env = "None detected"
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {vir_env}")
        print()
        print("WARNING: you're in the global envirnment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print()
        print("then run this program again.")

    else:
        vir_env = os.path.basename(sys.prefix)
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {vir_env}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated envirnment!")
        print("Safe to install packages without affecting the global system")
        print()
        paths = site.getsitepackages()
        if paths:
            print("Package installation path:")
            print(paths)


if __name__ == "__main__":
    try:
        check_matrix_status()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
