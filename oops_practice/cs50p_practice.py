class Student:
    def __init__(self, name: str, house: str):
        if not name:
            raise ValueError("missing name.")
        if house not in ["negi", "rastogi"]:
            raise ValueError("invalid house")

        self.name = name
        self.house = house

    def __str__(self) -> str:
        return f"i do some bullshit"


def student_getter() -> Student:
    while True:
        name = input("name:")
        house = input("house:")
        try:
            student = Student(name, house)
        except ValueError as e:

            print(e)
        else:
            break

    return student


def main() -> None:
    student = student_getter()
    print(f"{student.name} is from {student.house}")
    print(student)


if __name__ == "__main__":
    main()
