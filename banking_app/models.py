from datetime import datetime


class Transaction:
    def __init__(
        self,
        transaction_type: str,
        amount: float,
        note: str,
    ) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        self.note = note
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp} {self.transaction_type} {self.amount} - {self.note}"


class Account:
    def __init__(self, name: str, account_id: int, balance: float):
        self.name = name
        self.account_id = account_id
        self.__balance = balance
        self.__transaction_history = []
        self.__transaction_history.append(
            Transaction("deposit", balance, "created and deposited")
        )

    def get_balance(self) -> float:
        return self.__balance

    def get_history(self) -> list[Transaction]:
        return self.__transaction_history

    def deposit(self, money: float) -> dict[str, float | str]:
        if money <= 0:
            raise ValueError("money is too less to deposit")
        self.__balance += money
        self.__transaction_history.append(
            Transaction("deposit", money, "money deposited")
        )
        return {"message": "money deposited", "balance": self.get_balance()}

    def withdraw(self, money: float):
        if self.get_balance() < money:
            raise ValueError("insufficient balance")
        self.__balance -= money
        self.__transaction_history.append(
            Transaction("withdraw", money, "money withdrawn")
        )
        return {"message": "money withdrawn", "balance": self.get_balance()}
