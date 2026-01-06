import csv

PASS_MARK = 35

def get_grade(avg):
    if avg >= 90:
        return "A"
    if avg >= 75:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 50:
        return "D"
    return "F"

def load_students(filename):
    students = []
    grade_summary = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    with open(filename, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                maths = int(row["maths"])
                science = int(row["science"])
                english = int(row["english"])

                total = maths + science + english
                average = total / 3

                subject_passed = (
                    maths >= PASS_MARK
                    and science >= PASS_MARK
                    and english >= PASS_MARK
                )

                grade = get_grade(average)
                result = "PASS" if subject_passed and average >= 50 else "FAIL"

                student = {
                    "roll": row["roll_no"],
                    "name": row["name"],
                    "total": total,
                    "average": round(average, 2),
                    "grade": grade,
                    "result": result,
                }

                students.append(student)
                grade_summary[grade] += 1

            except ValueError:
                print(f"Skipping invalid record for student: {row['name']}")

    return students, grade_summary

def get_topper(students):
    topper = students[0]
    for s in students:
        if s["average"] > topper["average"]:
            topper = s
    return topper

def display_report(students, grade_summary):
    print("\nStudent Marks Report")
    print("-" * 70)
    print(f"{'Roll':<8}{'Name':<15}{'Total':<10}{'Average':<10}{'Grade':<8}{'Result'}")
    print("-" * 70)

    for s in students:
        print(
            f"{s['roll']:<8}"
            f"{s['name']:<15}"
            f"{s['total']:<10}"
            f"{s['average']:<10}"
            f"{s['grade']:<8}"
            f"{s['result']}"
        )

    print("-" * 70)

    topper = get_topper(students)
    print(f"\nClass Topper: {topper['name']} (Average: {topper['average']})")

    print("\nGrade Distribution:")
    for grade in grade_summary:
        print(f"{grade}: {grade_summary[grade]}")

def save_report(students, grade_summary):
    with open("report.txt", "w") as f:
        f.write("Student Marks Report\n")
        f.write("-" * 60 + "\n")

        for s in students:
            f.write(
                f"{s['roll']} | {s['name']} | "
                f"Total: {s['total']} | Avg: {s['average']} | "
                f"Grade: {s['grade']} | Result: {s['result']}\n"
            )

        topper = get_topper(students)
        f.write(f"\nClass Topper: {topper['name']} ({topper['average']})\n")

        f.write("\nGrade Distribution:\n")
        for grade in grade_summary:
            f.write(f"{grade}: {grade_summary[grade]}\n")

def main():
    students, grade_summary = load_students("students.csv")

    if not students:
        print("No valid student records found.")
        return

    display_report(students, grade_summary)
    save_report(students, grade_summary)

    print("\nReport saved to report.txt")

if __name__ == "__main__":
    main()