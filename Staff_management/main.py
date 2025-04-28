from staff import Staff
from manager import Manager
from company import Company

def main():
    cty = Company()

    while True:
        print("\n--- MENU ---")
        print("1. Thêm nhân viên thường")
        print("2. Thêm quản lý")
        print("3. Hiển thị tất cả nhân viên")
        print("4. Tìm nhân viên theo mã")
        print("5. Tính tổng quỹ lương công ty")
        print("6. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            ma_nv = input("Nhập mã nhân viên: ")
            ten = input("Nhập tên nhân viên: ")
            luong_co_ban = float(input("Nhập lương cơ bản: "))
            nv = Staff(ma_nv, ten, luong_co_ban)  # Giả sử lớp Staff
            cty.add_staff(nv)
            print("Đã thêm nhân viên thành công!")

        elif choice == '2':
            ma_nv = input("Nhập mã quản lý: ")
            ten = input("Nhập tên quản lý: ")
            luong_co_ban = float(input("Nhập lương cơ bản: "))
            he_so_chuc_vu = float(input("Nhập hệ số chức vụ: "))
            ql = Manager(ma_nv, ten, luong_co_ban, he_so_chuc_vu) # Giả sử lớp Manager
            cty.add_staff(ql)
            print("Đã thêm quản lý thành công!")

        elif choice == '3':
            print("\n--- Danh sách nhân viên ---")
            cty.show_staff()

        elif choice == '4':
            ma_nv_tim = input("Nhập mã nhân viên cần tìm: ")
            nv = cty.find_by_id(ma_nv_tim)
            if nv:
                print("Thông tin nhân viên:")
                print(nv)
            else:
                print("Không tìm thấy nhân viên có mã", ma_nv_tim)

        elif choice == '5':
            tong_luong = cty.cal_salary()
            print("Tổng quỹ lương công ty:", tong_luong)

        elif choice == '6':
            print("Thoát chương trình. Hẹn gặp lại!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
