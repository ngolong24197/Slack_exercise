from staff import Staff
from manager import Manager

class Company:
    def __init__(self):
        self.staff_list = []

    def add_staff(self, staff):

        self.staff_list.append(staff)

    def show_staff(self):

        for staff in self.staff_list:
            print(staff)

    def find_by_id(self, staffcode):

        for staff in self.staff_list:
            if staff.get_staffcode() == staffcode:
                return staff
        return None

    def cal_salary(self):

        total_salary = 0
        for staff in self.staff_list:
            total_salary += staff.get_salary()
        return total_salary
