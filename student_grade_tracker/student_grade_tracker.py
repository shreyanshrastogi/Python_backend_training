import json
from pathlib import Path


def student_grade_tracker():

    path = Path("grades.json")
    if not path.exists():
        grade = {"students": []}
        path.write_text(json.dumps(grade))
    else:
        with path.open("r") as f:
            grade = json.load(f)
    while True:
        student_name = input("Input Student name:")
        student_score = int(input("Input Student score:"))
        new_student = {"name": student_name, "score": student_score}
        grade["students"].append(new_student)
        quit = int(input("enter -1 to quit or any other num to continue:"))
        if quit == -1:
            break

    with path.open("w") as f:
        json.dump(grade, f, indent=4)


def main() -> None:
    student_grade_tracker()


if __name__ == "__main__":
    main()
