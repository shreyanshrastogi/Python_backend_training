from datetime import date
from pathlib import Path


def diary(entry: str, today: str) -> None:

    diary = Path("diary.txt")
    with diary.open("a") as f:
        f.write(f"\n{today}\n")
        f.write(entry)


if __name__ == "__main__":
    today = date.today().strftime("%d/%m/%y")
    entry = input(f"enter {today} entry:")

    diary(entry=entry, today=today)
