from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    The abstract class that provides a template
    for the classes that inherits this
    """
    def __init__(self) -> None:
        self.data_pro: list[str] = []
        self.counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise TypeError

    def output(self) -> tuple[int, str]:
        if not self.data_pro:
            raise ValueError("No more data to be parsed to output")
        cur_data: tuple[int, str] = (self.counter, self.data_pro[0])
        self.counter += 1
        self.data_pro.remove(self.data_pro[0])
        return cur_data


class NumericProcessor(DataProcessor):
    """
    Takes in ints floats or a list of both and outputs
    """
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            data = [data]
        for i in data:
            if not isinstance(i, (int, float)):
                return False
        return True

    def ingest(self, data: (int | float | list[int | float])) -> None:
        super().ingest(data)
        if isinstance(data, (int, float)):
            data = [data]
        self.data_pro = list(map(str, data))


class TextProcessor(DataProcessor):
    """
    Takes in valid values that are either strings
    or a list of strings and outputs
    """
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return (all(isinstance(i, str) for i in data))
        return False

    def ingest(self, data: (str | list[str])) -> None:
        super().ingest(data)
        if isinstance(data, str):
            data = [data]
        self.data_pro = data


class LogProcessor(DataProcessor):
    """
    Takes in valid values that are formated as a dictionary
    of strings and outputs
    """
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            data = [data]
        for data_dict in data:
            if not isinstance(data_dict, dict):
                return False
            if not all(isinstance(key, str) and isinstance(value, str)
                       for key, value in data_dict.items()):
                return False
        return True

    def ingest(self, data: (dict[str, str] | list[dict[str, str]])) -> None:
        super().ingest(data)
        if isinstance(data, dict):
            data = [data]
        for messages in data:
            temp_str: str = ""
            for message in messages.values():
                temp_str = temp_str + message
                if temp_str is message:
                    temp_str = temp_str + ": "
            self.data_pro.append(temp_str)


if __name__ == "__main__":
    print("=== Code Nexus - Date Processor ===\n")
    print("Testing Numeric Processor...")
    numpro = NumericProcessor()
    test: list[int | str] = [42, "Hello"]
    for i in test:
        print(f"Trying to validate input '{i}': {numpro.validate(i)}")
    try:
        print("Test invalid ingestion of string 'foo' without prior "
              "validation:")
        numpro.ingest("foo")
    except TypeError:
        print("Got exception: Improper numeric data")
    data_int: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_int}")
    numpro.ingest(data_int)
    print("Exctracting 3 values...")
    try:
        while numpro.counter < 3:
            num, string = numpro.output()
            print(f"Numeric value {num}: {string}")
    except ValueError as message:
        print(message)
    print("\nTesting Text Processor...")
    textpro = TextProcessor()
    print(f"Trying to validate input '42': {textpro.validate(42)}")
    data_str: list[str] = ["Hello", "Nexus", "World"]
    print(f"Processing data: {data_str}")
    textpro.ingest(data_str)
    print("Exctracting 1 value...")
    try:
        while textpro.counter < 1:
            num, string = textpro.output()
            print(f"Text value {num}: {string}")
    except ValueError as message:
        print(message)
    print("\nTesting Log Processor...")
    logpro = LogProcessor()
    print(f"Trying to validate input 'Hello': {logpro.validate("Hello")}")
    data: list[dict[str, str]] = [{'log_level': 'NOTICE', 'log_message':
                                   ' Connection to server'},
                                  {'log_level': 'ERROR', 'log_message':
                                   ' Unauthorized access!!'}]
    print(f"Processing data: {data}")
    logpro.ingest(data)
    print("Exctracting 2 value...")
    try:
        while logpro.counter < 2:
            num, string = logpro.output()
            print(f"Log entry {num}: {string}")
    except ValueError as message:
        print(message)
