import csv

PASS_MARK = 35


def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def load_students(filename):
    students = []
    grade_summary = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    with open(filename, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                maths = int(row.get("maths", 0))
                science = int(row.get("science", 0))
                english = int(row.get("english", 0))

                total = maths + science + english
                average = round(total / 3, 2)

                subject_status = {
                    "maths": "PASS" if maths >= PASS_MARK else "FAIL",
                    "science": "PASS" if science >= PASS_MARK else "FAIL",
                    "english": "PASS" if english >= PASS_MARK else "FAIL",
                }

                subject_passed = all(mark >= PASS_MARK for mark in [maths, science, english])

                grade = get_grade(average)
                result = "PASS" if subject_passed and average >= 50 else "FAIL"

                student = {
                    "roll": row.get("roll_no", "N/A"),
                    "name": row.get("name", "Unknown"),
                    "total": total,
                    "average": average,
                    "grade": grade,
                    "result": result,
                    "subjects": subject_status,
                }

                students.append(student)
                grade_summary[grade] += 1

            except ValueError:
                print(f"Skipping invalid record for student: {row.get('name', 'Unknown')}")

    return students, grade_summary


def get_topper(students):
    return max(students, key=lambda s: s["average"])


def class_statistics(students):
    total_avg = sum(s["average"] for s in students)
    pass_count = sum(1 for s in students if s["result"] == "PASS")

    return {
        "class_average": round(total_avg / len(students), 2),
        "pass_percentage": round((pass_count / len(students)) * 100, 2),
    }


def display_report(students, grade_summary):
    students.sort(key=lambda s: s["average"], reverse=True)

    print("\nSTUDENT MARKS REPORT")
    print("-" * 85)
    print(f"{'Roll':<8}{'Name':<15}{'Total':<10}{'Average':<10}{'Grade':<8}{'Result'}")
    print("-" * 85)

    for s in students:
        print(
            f"{s['roll']:<8}"
            f"{s['name']:<15}"
            f"{s['total']:<10}"
            f"{s['average']:<10}"
            f"{s['grade']:<8}"
            f"{s['result']}"
        )

    print("-" * 85)

    topper = get_topper(students)
    stats = class_statistics(students)

    print(f"\n🏆 Class Topper: {topper['name']} (Average: {topper['average']})")
    print(f"📊 Class Average: {stats['class_average']}")
    print(f"✅ Pass Percentage: {stats['pass_percentage']}%")

    print("\nGrade Distribution:")
    for grade, count in grade_summary.items():
        print(f"{grade}: {count}")


def save_txt_report(students, grade_summary):
    with open("report.txt", "w") as f:
        f.write("STUDENT MARKS REPORT\n")
        f.write("-" * 70 + "\n")

        for s in students:
            f.write(
                f"{s['roll']} | {s['name']} | "
                f"Total: {s['total']} | Avg: {s['average']} | "
                f"Grade: {s['grade']} | Result: {s['result']}\n"
            )

        topper = get_topper(students)
        stats = class_statistics(students)

        f.write(f"\nClass Topper: {topper['name']} ({topper['average']})\n")
        f.write(f"Class Average: {stats['class_average']}\n")
        f.write(f"Pass Percentage: {stats['pass_percentage']}%\n")

        f.write("\nGrade Distribution:\n")
        for grade, count in grade_summary.items():
            f.write(f"{grade}: {count}\n")


def main():
    students, grade_summary = load_students("students.csv")

    if not students:
        print("No valid student records found.")
        return

    display_report(students, grade_summary)
    save_txt_report(students, grade_summary)

    print("\n📁 Report generated:")
    print("✔ report.txt")


if __name__ == "__main__":
    main()
