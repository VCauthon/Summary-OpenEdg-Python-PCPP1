from uuid import uuid4


class AccountException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(f"ACCOUNT EXCEPTION: {message}")


class Account:
    def __init__(self) -> None:
        self.__account_number = str(uuid4())
        self.__current_balance = 0

    @property
    def account(self) -> str:
        return self.__account_number

    @account.setter
    def account(self, *args, **kwargs) -> None:
        raise AccountException('Number can be changed')

    @account.deleter
    def account(self) -> None:
        self.__check_if_can_be_deleted()

    @property
    def balance(self) -> int:
        return self.__current_balance

    @balance.setter
    def balance(self, amount: int) -> None:
        # Sanity check
        if not isinstance(amount, int):
            raise AccountException('Only accepts money deposits/withdrawal')

        # Check if the account can make this operation
        results_operation = self.__current_balance + amount
        if results_operation < 0:
            raise AccountException('Cannot be left with a negative balance')
        else:
            if amount > 100000 or amount < 100000:
                print("The amount of the transaction will be audited on the account.")
            self.__current_balance = results_operation

    @balance.deleter
    def balance(self) -> None:
        self.__check_if_can_be_deleted()

    def __check_if_can_be_deleted(self):
        if self.balance != 0:
            raise AccountException("There is still balance in the account to delete it")
        else:
            print("Account deleted")
            del self.__account_number
            del self.__current_balance


obj = Account()
# Setting the balance to 1000;
obj.balance = 1000
print(obj.balance)
# Trying to set the balance to -200;
try:
    obj.balance = -1200
except Exception as err:
    print(err)
# Trying to set a new value for the account number;
try:
    obj.account = "New number"
except Exception as err:
    print(err)
print(obj.account)
# Trying to deposit 1.000.000;
obj.balance = 1000000
# Trying to delete the account attribute containing a non-zero balance.
try:
    del obj.account
except Exception as err:
    print(err)

obj.balance = -1001000
del obj.account