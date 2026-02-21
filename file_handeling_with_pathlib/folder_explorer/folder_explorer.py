from pathlib import Path


def folder_explorer(path: str) -> None:
    folder = Path(path)
    if folder.exists():
        for item in folder.glob("*.txt"):
            print(item)
    else:
        print("folder does not exist.")


if __name__ == "__main__":
    path = input("Enter path of folder:")

    folder_explorer(path=path)
