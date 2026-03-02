import models
import repository


class BankServices:

    def __init__(self, db: repository.AccountDB):
        self.db = db

    def create_account(self, name: str, account_id: int, balance: float):
        account: models.Account = models.Account(
            name=name, account_id=account_id, balance=balance
        )
        self.db.add_account(account)

    def deposit(self, account_id: int, amount: float):

        self.db.get_account(account_id=account_id).deposit(amount)

    def withdraw(self, account_id: int, amount: float):
        self.db.get_account(account_id=account_id).withdraw(amount)

    def transfer(
        self, sender_id: int, receiver_id: int, amount: float
    ) -> dict[str, str | models.Account]:
        sender = self.db.get_account(sender_id)
        receiver = self.db.get_account(receiver_id)

        sender.withdraw(amount)
        receiver.deposit(amount)
        return {
            "message": f"{amount} transferred successfully",
            "from": sender,
            "To": receiver,
        }

    def get_balance(self, account_id: int) -> float:
        return self.db.get_account(account_id).get_balance()

    def get_all_account(self) -> dict[int, models.Account]:
        return self.db.get_all_accounts()

    def get_history(self, account_id: int) -> list[models.Transaction]:
        return self.db.get_account(account_id=account_id).get_history()

    def get_account(self, account_id: int) -> models.Account:
        return self.db.get_account(account_id=account_id)
