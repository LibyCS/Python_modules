from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """
    The abstract class that provides a template
    for the classes that inherits this
    """
    def __init__(self) -> None:
        """
        data_pro is the strings that have been processed
        counter is the index of the string, needs to be
        tracked when outputing it in the tuple
        """
        self.data_pro: list[str] = []
        self.counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Determines weather the type of data is
        correct for the processor to take in
        Empty for now must be overwritten in
        the child processor
        """
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """
        Takes in the data raises an error
        if the data type is not valid
        depending on the processor
        stores the data in a class variable list
        """
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
        """
        Determines weather the type of data is
        correct for the processor to take in
        """
        if not isinstance(data, list):
            data = [data]
        for i in data:
            if not isinstance(i, (int, float)):
                return False
        return True

    def ingest(self, data: (int | float | list[int | float])) -> None:
        """
        Takes in the data raises an error
        if the data type is not valid
        depending on the processor
        stores the data in a class variable list
        """
        super().ingest(data)
        if isinstance(data, list):
            for i in data:
                self.data_pro.append(str(i))
        else:
            self.data_pro.append(str(data))


class TextProcessor(DataProcessor):
    """
    Takes in valid values that are either strings
    or a list of strings and outputs
    """
    def validate(self, data: Any) -> bool:
        """
        Determines weather the type of data is
        correct for the processor to take in
        """
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return (all(isinstance(i, str) for i in data))
        return False

    def ingest(self, data: (str | list[str])) -> None:
        """
        Takes in the data raises an error
        if the data type is not valid
        depending on the processor
        stores the data in a class variable list
        """
        super().ingest(data)
        if isinstance(data, list):
            for text in data:
                self.data_pro.append(text)
        else:
            self.data_pro.append(data)


class LogProcessor(DataProcessor):
    """
    Takes in valid values that are formated as a dictionary
    of strings and outputs
    """
    def validate(self, data: Any) -> bool:
        """
        Determines weather the type of data is
        correct for the processor to take in
        """
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
        """
        Takes in the data raises an error
        if the data type is not valid
        depending on the processor
        stores the data in a class variable list
        """
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


class DataStream():
    """
    Registers the processors if given, keeps track of stats
    aswell as determining which registered processor
    should handle which data type
    """
    def __init__(self) -> None:
        """
        Stores all the processors in a list
        """
        self.processors: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        """
        Takes in any class that is a child of the abc
        DataProcessor and appends them to the class
        variable list of processors
        """
        self.processors.update({proc: 0})

    def process_stream(self, stream: list[Any]) -> None:
        """
        Analyzes each element in the list and sends them
        to the appropriate registered processor, raises error
        if no processor is adequate.
        """
        for data in stream:
            for proc in self.processors.keys():
                if proc.validate(data) is True:
                    proc.ingest(data)
                    if isinstance(data, list):
                        self.processors[proc] += len(data)
                    else:
                        self.processors[proc] += 1
                    break
            if proc.validate(data) is False:
                print("DataStream error - Can't process"
                      f" element in stream: {data}")

    def print_processors_stats(self) -> None:
        """
        Prints the stats for how many datas were processed
        by the registered processors
        """
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors.keys():
            if isinstance(proc, NumericProcessor):
                print("Numeric Processor: ", end="")
            elif isinstance(proc, TextProcessor):
                print("Text Processor: ", end="")
            elif isinstance(proc, LogProcessor):
                print("Log Processor: ", end="")
            else:
                print("Unknown Processor: ", end="")
            print(f"total {self.processors[proc]} items processed, "
                  f"remaining {len(proc.data_pro)} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Date Stream ===\n")
    print("Initalise Data Stream...")
    stream = DataStream()
    nums = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    stream.register_processor(nums)
    data = ['Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
            42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)
    stream.print_processors_stats()
    print("\n Registering other data processors")
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(data)
    stream.print_processors_stats()
    print("\nConsume some elements from the data processors:"
          "Numeric 3, Text 2, Log 1")
    processors = [nums, text, log]
    while processors:
        for proc in processors:
            proc.output()
        processors.remove(processors[-1])
    stream.print_processors_stats()
