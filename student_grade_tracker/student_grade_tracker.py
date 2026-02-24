import json
from pathlib import Path


def student_grade_tracker() -> None:
    # accessing grades.json if exists
    path = Path("grades.json")
    # if not exists make a new one
    if not path.exists():
        grade = {"students": []}
        path.write_text(json.dumps(grade))
    else:
        with path.open("r") as f:
            grade = json.load(f)
    # adding values in json
    while True:
        student_name: str = input("Input Student name:")
        student_score: float = float(input("Input Student score:"))
        new_student = {"name": student_name, "score": student_score}
        detect_exist = False
        # checking if student already exist in json
        for student in grade["students"]:
            if student_name == student["name"]:
                print("student already exists.")
                detect_exist = True
        if not detect_exist:
            grade["students"].append(new_student)

        quit = int(input("enter -1 to quit or any other num to continue:"))
        if quit == -1:
            break
    # finding top scorer and avg score from grade json
    avg_score: float = 0
    top_student: str = ""
    top_score: float = 0

    for student in grade["students"]:
        avg_score += student["score"]
        if student["score"] > top_score:
            top_student = student["name"]
            top_score = student["score"]

    try:

        avg_score //= len(grade["students"])
    except ZeroDivisionError:
        print("no students for avg")

    print("average score:", avg_score)
    print(f"top scorer {top_student} with {top_score} marks")

    # writing all data in grade.json

    with path.open("w") as f:
        json.dump(grade, f, indent=4)


def main() -> None:
    student_grade_tracker()


if __name__ == "__main__":
    main()
