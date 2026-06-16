#!/usr/bin/env python3

import sys
import os


if __name__ == "__main__":
    try:
        machine = sys.base_prefix
        current = sys.prefix
        version = str(sys.version_info.major) + "." + str(
            sys.version_info.minor)

        if machine == current:
            print("MATRIX STATUS: You're still plugged in\n")
            print(f"Current Python: {sys.executable}")
            print("Virtual Enviroment: None detected\n\n"
                  "WARNING: You're in the global environment!\n"
                  "The machines can see everything you install.\n\n"
                  "To enter the construct, run:\n"
                  "python -m venv matrix_env\n"
                  "source matrix_env/bin/activate # On Unix\n"
                  "matrix_env\\Scripts\\activate # On Windows\n\n"
                  "Then run this program again.")
        else:
            print("MATRIX STATUS: Welcome to the construct\n\n"
                  f"Current Python: {sys.executable}\n"
                  f"Virtual Environment: {current.split("/")[-1]}\n"
                  f"Environment Path: {current}\n\n"
                  "SUCCESS: You're in an isolated environment!\n"
                  "Safe to install packages without affecting the global"
                  " system.\n\nPackage installation path:")
            if os.path.exists(f"{current}/lib/python{version}/site-packages"):
                print(f"{current}/lib/{version}/site-packages")
    except Exception as err:
        print(err)
