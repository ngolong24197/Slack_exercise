

from function import *
def main():
    contacts = {}

    while True:
        print("\n--- Quản lý danh bạ ---")
        print("1. Thêm liên hệ")
        print("2. Xem thông tin liên hệ")
        print("3. Sửa thông tin liên hệ")
        print("4. Xóa liên hệ")
        print("5. Hiển thị toàn bộ liên hệ")
        print("6. Tìm kiếm theo số điện thoại hoặc email")
        print("7. Đếm số lượng liên hệ")
        print("0. Thoát")

        choice = input("Chọn chức năng (0-7): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contact(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            display_all_contacts(contacts)
        elif choice == '6':
            search_contact(contacts)
        elif choice == '7':
            count_contacts(contacts)
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
