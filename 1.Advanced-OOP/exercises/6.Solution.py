
class Scanner:
    @classmethod
    def scan(cls) -> None:
        print('scan() method from Scanner class')

class Printer:
    @classmethod
    def print(cls) -> None:
        print('print() method from Printer class')

class Fax:
    @classmethod
    def send(cls) -> None:
        print('send() method from Fax class')
    @classmethod
    def print(cls) -> None:
        print('print() method from Fax class')

class MFD_SPF(Scanner, Printer, Fax):
    pass


class MFD_SFP(Scanner, Fax, Printer):
    pass


# Calling all the class methods
print('Calling methods from MFD_SPF'.center(80, '*'))
MFD_SPF.scan()
MFD_SPF.print()
MFD_SPF.send()

print('Calling methods from MFD_SFP'.center(80, '*'))
MFD_SFP.scan()
MFD_SFP.print()
MFD_SFP.send()