student_grades = { }

# add the student name and grade of student_grades Dict
def add_student(name, grade):
    student_grades[name]=grade
    print(f"Added {name} with a {grade}")
# update the student name and grade of student_grades Dict
def update_student(name, grade):
    if(name in student_grades):
        student_grades[name]=grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found !")
# delete the student name  of student_grades Dict
def delete_student(name):
    if(name in student_grades):
        del student_grades[name]
        print(f"{name} has been successfully")
    else:
        print(f"{name} is not found !")

# View on  the student name and grade of student_grades Dict
def display_all_students():
    if(student_grades):
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No students Found/added")

# check the condition is true
def main():
    while True:
        print("\n Student Grade Management System")
        print("!. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if(choice == 1):
            name = input("Enter student name = ")
            grade = input("Enter Student grade = ")
            add_student(name, grade)

        elif(choice==2):
            name = input("Enter student name = ")
            grade = input("Enter Student grade = ")
            update_student(name, grade)

        elif(choice==3):
            name = input("Enter student name = ")
            grade = input("Enter Student grade = ")
            delete_student(name,grade)

        elif(choice==4):
            display_all_students()
        elif(choice == 5):
            print("Closing the Program..")
            break
        else:
            print("Invalid Choice")
main()