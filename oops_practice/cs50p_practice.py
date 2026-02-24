class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def student_getter():
    name = input("enter name:")
    house = input("input house:")

    return Student(name, house)


def main():
    student = student_getter()
    print(f"{student.name} is from {student.house}")


if __name__ == "__main__":
    main()
