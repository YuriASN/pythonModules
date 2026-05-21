#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.data: list[str] = []
        self.extracts: int = 0

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def output(self) -> tuple[int, str]:
        poped = self.extracts
        self.extracts += 1
        return (poped, self.data.pop(0))


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def ingest(
            self,
            data: int | float | list[int | float] | list[int] | list[float]
            ) -> None:
        if not self.validate(data):
            raise Exception("Imporoper numeric data")
        try:
            if isinstance(data, list):
                for value in data:
                    self.data.append(str(value))
            else:
                self.data.append(str(data))
        except Exception as err:
            raise Exception(f"Ingesting numeric data: {err}")

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, (int, float)):
                return True
            if isinstance(data, list):
                return all(isinstance(value, (int, float)) for value in data)
            return False
        except Exception as err:
            raise err


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        try:
            if isinstance(data, list):
                self.data += [value for value in data]
            else:
                self.data.append(data)
        except Exception as err:
            print(err)

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, str):
                return True
            if isinstance(data, list):
                return all(isinstance(value, str) for value in data)
            return False
        except Exception as err:
            raise err


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:

        def get_value(data: dict[str, str]) -> list[str]:
            value: list = [v for v in data.values()]
            return value

        try:
            if not self.validate(data):
                raise Exception("Data type isn't 'Log'")
            if isinstance(data, list):
                for each in data:
                    value = get_value(each)
                    self.data.append(f"{(value[0])}: {value[1]}")
            else:
                value = get_value(data)
                self.data.append(f"{value[0]}: {value[1]}")
        except Exception as err:
            print(err)

    def validate(self, data: Any) -> bool:

        def is_str_dict(d: dict) -> bool:
            return all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in d.items()
                )

        try:
            if isinstance(data, dict):
                return is_str_dict(data)
            if isinstance(data, list):
                return all(
                    isinstance(each, dict) and is_str_dict(each)
                    for each in data
                )
            return False
        except Exception as err:
            raise err


if __name__ == "__main__":
    nump = NumericProcessor()
    textp = TextProcessor()
    logp = LogProcessor()

    print("=== Code Nexus - Data Processor ===\n")
    # Numeric
    try:
        print("Testing numeric processor...")
        print(f" Trying to validate input '42': {nump.validate(42)}")
        print(f" Trying to validate input 'hello': {nump.validate('hello')}")
        print(" Test invalid ingestion of string 'foo' without " +
              "prior validation:")
        nump.ingest("foo")  # lint error stated on subject end of page 7
    except Exception as err:
        print(f" Got exception: {err}")
    try:
        num_data = [1, 2, 3, 4, 5]
        print(f" Processing data: {num_data}")
        nump.ingest(num_data)
        returned_data = nump.output
        print(" Extracting 3 values...")
        for i in range(3):
            index, value = nump.output()
            print(f" Numeric value {index}: {value}")
    except Exception as err:
        print(f"Got exception: {err}")

    print()
    # Text
    try:
        print("Testing Text processor...")
        print(f" Trying to validate input '42': {textp.validate(42)}")
        print(f" Trying to validate input 'hello': {textp.validate('hello')}")
        print(" Test invalid ingestion of int '42' without " +
              "prior validation:")
        textp.ingest(42)  # lint error stated on subject end of page 7
    except Exception as err:
        print(f" Got exception: {err}")
    try:
        text_data = ['Hello', '2 gether', 'Nexus', 'World']
        print(f" Processing data: {text_data}")
        textp.ingest(text_data)
        returned_data = textp.output
        print(" Extracting 2 values...")
        for i in range(2):
            index, value = textp.output()
            print(f" Text value {index}: {value}")
    except Exception as err:
        print(f" Got exception: {err}")

    print()
    # Log
    try:
        print("Testing Log processor...")
        print(f" Trying to validate input '42': {logp.validate(42)}")
        print(f" Trying to validate input 'hello': {logp.validate('hello')}")
        log_data = [{'log_level': 'NOTICE',
                     'log_message': 'Connection to server'},
                    {'log_level': 'ERROR',
                     'log_message': 'Unauthorized access!!'}]
        print(f" Processing data: {log_data}")
        logp.ingest(log_data)
        returned_data = logp.output
        print(" Extracting 2 values...")
        for i in range(2):
            index, value = logp.output()
            print(f" Log entry {index}: {value}")
    except Exception as err:
        print(f" Got exception: {err}")
