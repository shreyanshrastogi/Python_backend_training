import models
import repository
import schemas
import service
from fastapi import FastAPI

app = FastAPI()
db = repository.AccountDB()
bank = service.BankServices(db)


# get_all_account
@app.get("/account")
def all_accounts() -> list[dict[str, str | int | float]]:
    accounts = bank.get_all_account()
    return [
        {"account_id": aid, "name": acc.name, "balance": acc.get_balance()}
        for aid, acc in accounts.items()
    ]


# transfer
@app.put("/account/transfer")
def transfer(
    account_details: schemas.TransferSchema,
) -> dict[str, str | schemas.TransferSchema]:
    bank.transfer(
        account_details.sender_id, account_details.receiver_id, account_details.amount
    )
    return {"message": "transfer successful", "details": account_details}


# create account
@app.post("/account/create/{account_id}")
def create_account(
    account_id: int, account: schemas.Data
) -> dict[str, int | str | schemas.Data]:
    bank.create_account(
        account_id=account_id, name=account.name, balance=account.balance
    )
    return {
        "message": "bank account created successfully",
        "account_id": account_id,
        "account_details": account,
    }


# deposit
@app.put("/account/{account_id}/deposit")
def deposit(account_id: int, amount: schemas.AmountSchema) -> dict[str, str | float]:
    bank.deposit(account_id=account_id, amount=amount.amount)
    return {
        "message": "deposited successfully",
        "updated_balance": bank.get_balance(account_id=account_id),
    }


# withdraw
@app.put("/account/{account_id}/withdraw")
def withdraw(account_id: int, amount: schemas.AmountSchema) -> dict[str, str | float]:
    bank.withdraw(account_id=account_id, amount=amount.amount)
    return {
        "message": "money withdrawn successfully",
        "updated_balance": bank.get_balance(account_id=account_id),
    }


# get balance
@app.get("/account/{account_id}/balance")
def get_balance(account_id: int) -> dict[str, int | float]:
    balance = bank.get_balance(account_id)
    return {"account_id": account_id, "balance": balance}


# get_account
@app.get("/account/{account_id}")
def get_account(account_id: int) -> dict[str, str | int | float]:
    account = bank.get_account(account_id=account_id)
    return {
        "name": account.name,
        "account_id": account_id,
        "account_balance": bank.get_balance(account_id),
    }


# delete_account
@app.delete("/account/delete/{account_id}")
def delete_account(account_id: int) -> dict[str, str]:
    return bank.delete_account(account_id=account_id)


# get history
@app.get("/account/{account_id}/history")
def get_history(account_id) -> dict[str, list[str]]:
    history = bank.get_history(account_id=account_id)
    return {"history": [str(t) for t in history]}
