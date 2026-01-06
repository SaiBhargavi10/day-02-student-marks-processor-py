import csv

def is_valid_mark(mark):
    return 0 <= mark <= 100

def calculate_percentage(student):
    total = student["maths"] + student["science"] + student["english"]
    return (total / 300) * 100

def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    return "F"

def read_students(file_path):
    students = []

    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = {
                    "roll_no": int(row["roll_no"]),
                    "name": row["name"],
                    "maths": int(row["maths"]),
                    "science": int(row["science"]),
                    "english": int(row["english"])
                }

                if not all(is_valid_mark(student[sub])
                           for sub in ["maths", "science", "english"]):
                    print(f"Invalid marks for {student['name']}. Skipping.")
                    continue

                students.append(student)

    except FileNotFoundError:
        print("Student data file not found.")
    except ValueError:
        print("Invalid data format in file.")

    return students

def print_report(student):
    percentage = calculate_percentage(student)
    grade = assign_grade(percentage)
    total = student["maths"] + student["science"] + student["english"]

    print("-" * 40)
    print(f"Roll No     : {student['roll_no']}")
    print(f"Name        : {student['name']}")
    print(f"Total Marks : {total}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print("-" * 40)

def main():
    file_path = "../data/students.csv"
    students = read_students(file_path)

    if not students:
        print("No valid student records found.")
        return

    print("\nSTUDENT MARKS SUMMARY REPORT\n")

    for student in students:
        print_report(student)

    print("\nReport generated successfully.\n")

if __name__ == "__main__":
    main()