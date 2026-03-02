import repository
import service


def main() -> None:
    db = repository.AccountDB()
    bank = service.BankServices(db=db)

    while True:
        try:
            print(
                """Welcome to PyBank!
    1. Create account
    2. Deposit
    3. Withdraw
    4. Transfer
    5. Check balance
    6. Transaction history
    7. Exit
            """
            )
            choice = int(input("Enter choice:"))
            match choice:

                case 1:

                    name: str = input("name:")
                    account_id: int = int(input("enter id:"))
                    initial_balance: float = float(input("enter starting balance:"))
                    bank.create_account(
                        name=name, account_id=account_id, balance=initial_balance
                    )

                    print(
                        f"account created successfully \n{bank.get_account(account_id=account_id)}"
                    )

                case 2:

                    account_id: int = int(input("enter id:"))
                    amount: float = float(input("enter amount:"))
                    bank.deposit(account_id=account_id, amount=amount)
                    print(
                        f"money deposited  successfully \nupdated balance:{bank.get_balance(account_id=account_id)}"
                    )

                case 3:

                    account_id: int = int(input("enter id:"))
                    amount: float = float(input("enter amount:"))
                    bank.withdraw(account_id=account_id, amount=amount)
                    print(
                        f"money withdrawn  successfully \nupdated balance:{bank.get_balance(account_id=account_id)}"
                    )

                case 4:

                    sender_id: int = int(input("enter sender id:"))
                    receiver_id: int = int(input("enter receiver id:"))
                    amount: float = float(input("enter amount:"))
                    bank.transfer(
                        sender_id=sender_id, receiver_id=receiver_id, amount=amount
                    )

                    print(
                        f"money Transferred  successfully \nupdated balance:{bank.get_balance(account_id=sender_id)}"
                    )

                case 5:
                    account_id: int = int(input("enter id:"))
                    balance = bank.get_balance(account_id=account_id)
                    print(
                        f"{bank.get_account(account_id=account_id).name} with {account_id} has balance of {balance} Rs"
                    )
                case 6:
                    account_id: int = int(input("enter id:"))
                    history = bank.get_history(account_id=account_id)
                    for transaction in history:
                        print(transaction)

                case 7:
                    break

                case _:
                    print("invalid choice.")
        except ValueError as e:
            print(f"error:{e}")


if __name__ == "__main__":
    main()
