from ManagementApp import ManagementApp
from student import Student

def main():
    app = ManagementApp()
    
    print("Welcome to the Student Management System!!!")

    st = Student()


    app.addStudent(st)


    app.viewStudent(st)


    app.students.append(st)
    while True:
        print("\n====== Student Management Menu ======")
        print("1. Add a single student and view")
        print("2. Add list of students")
        print("3. Print list of students")
        print("4. Find the best student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            st = Student()
            app.addStudent(st)
            app.viewStudent(st)
        elif choice == '2':
            app.addListOfStudent()
        elif choice == '3':
            app.printListOfStudent()
        elif choice == '4':
            app.findTheBestStudent()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()