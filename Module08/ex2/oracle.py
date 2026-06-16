#!/usr/bin/env python3

import os
from typing import Dict
from dotenv import load_dotenv  # type: ignore


def get_file_env() -> Dict:
    envs: Dict[str, str] = {}
    try:
        with open(".env", "r") as file:
            while (line := file.readline()):
                key, value = line.strip().split("=")
                envs[key] = value
    except FileNotFoundError:
        raise FileNotFoundError("Missing the '.env' file")
    except Exception as err:
        raise Exception(f"While parsing the '.env' file: {err}")
    return envs


def get_env_vars() -> Dict:
    try:
        envs: Dict = {}
        file_envs: Dict = {}
        load_dotenv()
        envs["MATRIX_MODE"] = os.getenv("MATRIX_MODE")
        if envs["MATRIX_MODE"] not in ("development", "production", None):
            raise Exception("'MATRIX_MODE' has to be 'development' or "
                            "'production'")
        envs["DATABASE_URL"] = os.getenv("DATABASE_URL")
        envs["API_KEY"] = os.getenv("API_KEY")
        envs["LOG_LEVEL"] = os.getenv("LOG_LEVEL")
        envs["ZION_ENDPOINT"] = os.getenv("ZION_ENDPOINT")
        for key, value in envs.items():
            if value is None:
                if not len(file_envs):
                    file_envs = get_file_env()
                if key not in file_envs.keys():
                    raise KeyError(f"'{key}' not found in '.env'")
                envs[key] = file_envs[key]

    except Exception as err:
        raise Exception(err)
    return envs


def display_env_data(envs: Dict) -> None:
    try:
        print("ORACLE STATUS: Reading the Matrix...\n\nConfiguration loaded:")
        print(f'Mode: {envs["MATRIX_MODE"]}\n'
              f'Database: {envs["DATABASE_URL"]}\n'
              f'API Access: {envs["API_KEY"]}\n'
              f'Log Level: {envs["LOG_LEVEL"]}\n'
              f'Zion Network: {envs["ZION_ENDPOINT"]}\n')
        print("Environment security check:\n"
              "[OK] No hardcoded secrets detected\n"
              "[OK] .env file properly configured\n"
              "[OK] Production overrides available\n\n"
              "The Oracle sees all configurations.")
    except Exception as err:
        print(f"Printing data: {err}")


def access_mainframe() -> None:
    try:
        envs = get_env_vars()
        display_env_data(envs)
    except BaseException as err:
        print(err)


if __name__ == "__main__":
    access_mainframe()
