from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from uuid import uuid4


@dataclass
class Actions:
    class_used: type
    methods_called: List[str]


class Scanner(ABC):

    def __init__(self, max_resolution: str) -> None:
        self.scanner_max_resolution: str = max_resolution
        self.scanner_serial_number: str = str(uuid4())

    @abstractmethod
    def scan_document():
        pass

    @abstractmethod
    def get_scanner_status():
        pass


class Printer(ABC):

    def __init__(self, max_resolution: str) -> None:
        self.printer_max_resolution: str = max_resolution
        self.printer_serial_number: str = str(uuid4())

    @abstractmethod
    def print_document():
        pass

    @abstractmethod
    def get_printer_status():
        pass


# Not asked but ... let's not repeat the code
class PrinterHPActions(Printer):
    def get_printer_status(self):
        print("- Printer status:"
              f"\n\t> Max resolution: {self.printer_max_resolution} "
              f"\n\t> Serial Number: {self.printer_serial_number}")

    def print_document(self):
        print(f'- Document printed from {self.__class__.__name__}')


# Not asked but ... let's not repeat the code
class ScannerHPActions(Scanner):
    def get_scanner_status(self):
        print("- Scanner status:"
              f"\n\t> Max resolution: {self.scanner_max_resolution} "
              f"\n\t> Serial Number: {self.scanner_serial_number}")
    def scan_document(self):
        print(f'- Document scanned from {self.__class__.__name__}')


class MFD1(ScannerHPActions, PrinterHPActions):
    def __init__(self) -> None:
        max_resolution = "8MP"
        ScannerHPActions.__init__(self, max_resolution)
        PrinterHPActions.__init__(self, max_resolution)


class MFD2(ScannerHPActions, PrinterHPActions):
    def __init__(self) -> None:
        max_resolution = "12MP"
        ScannerHPActions.__init__(self, max_resolution)
        PrinterHPActions.__init__(self, max_resolution)
        self.print_history = 0

    def print_document(self):
        PrinterHPActions.print_document(self)
        self.print_history += 1

    def print_operation_history(self):
        print(f'- {self.print_history} impressions have been made')


class MFD3(ScannerHPActions, PrinterHPActions):
    def __init__(self) -> None:
        max_resolution = "48MP"
        ScannerHPActions.__init__(self, max_resolution)
        PrinterHPActions.__init__(self, max_resolution)
        self.print_history = 0

    def print_document(self):
        PrinterHPActions.print_document(self)
        self.print_history += 1

    def print_operation_history(self):
        print(f'- {self.print_history} impressions have been made')

    def retrieved_faxes(self):
        print("- You have receive a Fax!")


basic_methods = [
    'get_printer_status',
    'print_document',
    'get_scanner_status',
    'scan_document']


actions = [
    Actions(
        class_used=MFD1,
        methods_called=basic_methods
    ),
    Actions(
        class_used=MFD2,
        methods_called=basic_methods + [
            "print_operation_history",
            "print_document",
            "print_document",
            "print_operation_history"]
    ),
    Actions(
        class_used=MFD3,
        methods_called=basic_methods + [
            "print_operation_history",
            "print_document",
            "print_document",
            "print_operation_history",
            "retrieved_faxes"]
    ),
]


for element in actions:
    print(f"Actions done by {element.class_used.__name__}".center(80, "*"))
    # Creates an objet of the test
    obj = element.class_used()
    # Calls each method configured in actions
    for action in element.methods_called:
        getattr(obj, action)()
print("".center(80, "*"))