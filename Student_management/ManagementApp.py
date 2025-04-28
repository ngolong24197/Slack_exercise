from student import Student

class ManagementApp:
    def __init__(self):
        self.students = []
    
    def addStudent(self, st):
        st.set_student_Id(int(input("Enter student ID: ")))
        st.set_name(input("Enter student name: "))
        st.set_math(float(input("Enter Math mark: ")))
        st.set_physics(float(input("Enter Physic mark: ")))
        st.set_chemistry(float(input("Enter Chemistry mark: ")))

    def viewStudent(self, st):
        print(f"Student ID: {st.get_student_Id()}")
        print(f"Student Name: {st.get_name()}")
        print(f"Math: {st.get_math()}")
        print(f"Physic: {st.get_physics()}")
        print(f"Chemistry: {st.get_physics()}")
        print(f"Average Mark: {st.get_Average():.2f}")
        print(f"Rate: {st.getRate()}")

    def addListOfStudent(self):
        n = int(input("Enter number of students to add: "))
        for _ in range(n):
            st = Student()
            self.addStudent(st)
            self.students.append(st)
            
    def printListOfStudent(self):
        print("\n--- List of Students ---")
        for st in self.students:
            self.viewStudent(st)
        print("------------------------")
        print(f"Total number of students: {len(self.students)}")
        
    def findTheBestStudent(self):
        if not self.students:
            print("No students in the list.")
            return
        best_student = self.students[0]
        for st in self.students:
            if st.get_Average() > best_student.get_Average():
                best_student = st
        print("\n--- Best Student ---")
        self.viewStudent(best_student)
        print("-------------------")
        
           