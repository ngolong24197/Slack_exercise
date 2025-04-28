from staff import Staff

class Manager(Staff):
        
        
        def __init__(self,staffcode,name,salary,role_multiply):
            super().__init__(staffcode, name,salary)
            self.__role_multiply = role_multiply
            
            
        def cal_salary(self):
            return super().get_salary()*self.__role_multiply
            
        def __str__(self):
            return f"Ma nhan vien: {self.get_staffcode()}: Nhan vien {self.get_name()} co muc luong la {self.cal_salary()} , Vai tro: Quan ly"
        
        
        def get_role_multiply(self):
            return self.__role_multiply

    
        def set_role_multiply(self, role_multiply):
            self.__role_multiply = role_multiply
  
        def get_salary(self):
            return self.cal_salary()
            