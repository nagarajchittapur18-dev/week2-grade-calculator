# Name: Nagaraj Chittapur
# Project: Student Grade Calculator
# Description:
# This program collects student marks, calculates average,
# assigns grades with comments, displays results,
# allows searching students, and saves data to a file.


# Function to determine grade based on average marks
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


# Function to return comments based on grade
def get_comment(grade):
    if grade == "A":
        return "Excellent"
    elif grade == "B":
        return "Very Good"
    elif grade == "C":
        return "Good"
    elif grade == "D":
        return "Needs Improvement"
    else:
        return "Fail"


# Validate number of students
while True:
    try:
        num_students = int(input("Enter number of students: "))
        if num_students > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Enter a number.")

names = []
marks_list = []
results = []

# Collecting student data
for i in range(num_students):
    print(f"\nStudent {i + 1}")

    name = input("Enter student name: ").strip()
    names.append(name)

    subjects = []
    for j in range(3):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {j + 1}: "))
                if 0 <= mark <= 100:
                    subjects.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter numeric value.")

    marks_list.append(subjects)

# Calculate results
total_avg = 0
highest_avg = -1
lowest_avg = 101

for i in range(num_students):
    avg = sum(marks_list[i]) / 3
    grade = get_grade(avg)
    comment = get_comment(grade)

    results.append([names[i], marks_list[i], avg, grade, comment])

    total_avg += avg
    highest_avg = max(highest_avg, avg)
    lowest_avg = min(lowest_avg, avg)

class_average = total_avg / num_students

# Display results
colors = {
    "A": "\033[92m",
    "B": "\033[94m",
    "C": "\033[93m",
    "D": "\033[91m",
    "F": "\033[90m"
}
reset = "\033[0m"

print("\n" + "=" * 70)
print(f"{'Name':<12}{'Marks':<25}{'Avg':<8}{'Grade':<8}{'Comment'}")
print("=" * 70)

for r in results:
    color = colors[r[3]]
    print(f"{r[0]:<12}{str(r[1]):<25}{r[2]:<8.2f}{color}{r[3]:<8}{reset}{r[4]}")

print("=" * 70)
print(f"Class Average : {class_average:.2f}")
print(f"Highest Avg   : {highest_avg:.2f}")
print(f"Lowest Avg    : {lowest_avg:.2f}")
print("=" * 70)

# =========================
# Step 7: Extra Features
# =========================
while True:
    print("\nMENU")
    print("1. Search Student")
    print("2. Save Results to File")
    print("3. Exit")

    choice = input("Choose option (1-3): ").strip()

    if choice == "1":
        search_name = input("Enter student name to search: ").strip()
        found = False

        for r in results:
            if r[0].lower() == search_name.lower():
                print("\nStudent Found")
                print(f"Name   : {r[0]}")
                print(f"Marks  : {r[1]}")
                print(f"Average: {r[2]:.2f}")
                print(f"Grade  : {r[3]}")
                print(f"Comment: {r[4]}")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "2":
        try:
            with open("grade_results.txt", "w") as file:
                for r in results:
                    file.write(
                        f"Name:{r[0]} Marks:{r[1]} "
                        f"Avg:{r[2]:.2f} Grade:{r[3]} Comment:{r[4]}\n"
                    )
            print("Results successfully saved to grade_results.txt")
        except IOError:
            print("Error while saving file.")

    elif choice == "3":
        print("Thank you. Program ended.")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
