import models


class AccountDB:
    def __init__(self):
        self.__db = {}

    def add_account(self, account: models.Account) -> dict[str, str]:
        if account.account_id in self.__db:
            raise ValueError("account_id already exist")
        self.__db[account.account_id] = account
        return {"message": f"{account.account_id} added successfully"}

    def get_account(self, account_id: int) -> models.Account:
        if account_id not in self.__db:
            raise ValueError("account not available")

        return self.__db[account_id]

    def get_all_accounts(self) -> dict[int, models.Account]:
        return self.__db

    def delete_account(self, account_id: int) -> dict[str, str]:
        if account_id not in self.__db:
            raise ValueError("account not found")
        del self.__db[account_id]
        return {"message": f"{account_id} deleted successfully"}

    def account_exists(self, account_id: int) -> bool:
        if account_id in self.__db:
            return True
        else:
            return False
