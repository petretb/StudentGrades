import csv

# Function to add student data to a CSV file
def add_student_to_file(filename, student_data):
    file_exists = False
    try:
        with open(filename, 'r'):
            file_exists = True
    except FileNotFoundError:
        file_exists = False
    # student_data is expected to be a dictionary: {'id': '123', 'name': 'Alice', 'grade': 85, 'subject': 'Math'}
    with open(filename, 'a', newline='') as file:
        fieldnames = ['id','name','grade','subject']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(student_data)

def read_students_from_file(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['grade'] = int(row['grade'])  # Convert grade to integer
                students.append(row)
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    return students
def insertion_sort(students, key='grade'):
    for i in range(1, len(students)):
        current = students[i]
        j = i - 1
        while j >= 0 and students[j][key] > current[key]:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = current
    return students
def write_sorted_students_to_file(filename, students):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'name', 'grade', 'subject'])
        writer.writeheader()
        writer.writerows(students)
def linear_search(students, search_key, search_value):
    results = [student for student in students if student[search_key] == search_value]
    return results
def binary_search(students, search_key, search_value):
    low, high = 0, len(students) - 1
    while low <= high:
        mid = (low + high) // 2
        if students[mid][search_key] == search_value:
            return students[mid]
        elif students[mid][search_key] < search_value:
            low = mid + 1
        else:
            high = mid - 1
    return None


def main():
    filename = 'grades.csv'
    sorted_filename = 'sorted_grades.csv'

    while True:
        print("\nStudent Grades Management System")
        print("1. Add Student")
        print("2. View and Sort Students")
        print("3. Search for a Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Collect student data
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            grade = int(input("Enter Grade: "))
            subject = input("Enter Subject: ")
            add_student_to_file(filename, {'id': student_id, 'name': name, 'grade': grade, 'subject': subject})

        elif choice == '2':
            # Read, sort, and write sorted data
            students = read_students_from_file(filename)
            sorted_students = insertion_sort(students)
            write_sorted_students_to_file(sorted_filename, sorted_students)
            print(f"Data sorted and saved to {sorted_filename}")

        elif choice == '3':
            search_type = input("Choose search method (linear/binary): ").lower()
            search_key = input("Search by ID or Name? ").lower()
            search_value = input(f"Enter {search_key.capitalize()}: ")
            if search_key == 'grade':
                search_value = int(search_value)

            students = read_students_from_file(sorted_filename if search_type == 'binary' else filename)
            if search_type == 'binary':
                sorted_students = insertion_sort(students)
                result = binary_search(sorted_students, search_key, search_value)
            else:
                result = linear_search(students, search_key, search_value)

            if result:
                print("Student found:", result)
            else:
                print("Student not found.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
main()