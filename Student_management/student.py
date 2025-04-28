class Student():
    def __init__(self, studentId = 0, name = "", math =0.0, physics =0.0, chemistry =0.0):
        self.studentId = studentId
        self.name = name
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
        
    def get_student_Id(self):
        return self.studentId
    def set_student_Id(self, studentId):
        self.studentId = studentId
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_math(self):
        return self.math
    def set_math(self, math):
        self.math = math
    def get_physics(self):
        return self.physics
    def set_physics(self, physics):
        self.physics = physics
    def get_chemistry(self):
        return self.chemistry
    def set_chemistry(self,chemistry):
        self.chemistry = chemistry
    
    def get_Average(self):
        return (self.math + self.physics + self.chemistry) / 3
    def getRate(self):
        avg = self.get_Average()
        if avg >= 8.0:
            return "A"
        elif avg >= 6.5:
            return "B"
        elif avg >= 5.0:
            return "C"
        else:
            return "D"
    
                