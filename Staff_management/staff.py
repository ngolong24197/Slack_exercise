


class Staff:
    def __init__(self,staffcode,name,salary):
        self.__staffcode = staffcode
        self.__salary = salary
        self.__name = name
        
    def __str__(self):
        return f"Ma nhan vien: {self.__staffcode}: Nhan vien {self.__name} co muc luong la {self.__salary}"
    
    def get_staffcode(self):
        return self.__staffcode
    
    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
        
    def set_staffcode(self,staffcode):
        self.__staffcode = staffcode
        
    def set_name(self,name):
        self.__name = name

    def set_salary(self,salary):
        self.__salary = salary