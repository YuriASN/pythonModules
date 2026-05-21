#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Dict


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


class DataStream():
    def __init__(self) -> None:
        self.processors: Dict = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors[proc] = 0

    def process_stream(self, stream: list[Any]) -> None:
        for value in stream:
            ingested = False
            for proc in self.processors.keys():
                if proc.validate(value):
                    ingested = True
                    proc.ingest(value)
                    if isinstance(value, list):
                        self.processors[proc] += len(value)
                    else:
                        self.processors[proc] += 1
            if not ingested:
                print("DataStream error - Can't process element in "
                      f"stream: {value}")

    def print_processors_stats(self) -> None:
        if not len(self.processors):
            print("No processor found, no data")
            return
        for proc in self.processors.keys():
            if isinstance(proc, NumericProcessor):
                print(f"Numeric Processor: total {self.processors[proc]} items"
                      f" processed, remaining {len(proc.data)} on processor")
            elif isinstance(proc, TextProcessor):
                print(f"Text Processor: total {self.processors[proc]} items"
                      f" processed, remaining {len(proc.data)} on processor")
            elif isinstance(proc, LogProcessor):
                print(f"Log Processor: total {self.processors[proc]} items"
                      f" processed, remaining {len(proc.data)} on processor")


if __name__ == "__main__":
    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
        ]
    print("=== Code Nexus - Data Stream ===\n\nInitialize Data Stream...")
    stream = DataStream()
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print()

    print("Registering Numeric Processor\n")
    stream.register_processor(NumericProcessor())
    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print('\nRegistering other data processors')
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    print("Send the same batch again")
    stream.process_stream(data)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for proc in stream.processors.keys():
        if isinstance(proc, NumericProcessor):
            for i in range(3):
                proc.output()
        elif isinstance(proc, TextProcessor):
            for i in range(2):
                proc.output()
        elif isinstance(proc, LogProcessor):
            for i in range(1):
                proc.output()
    stream.print_processors_stats()
