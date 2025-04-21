from functions import *



def main():
    while True:
        print_menu()
        user_input = input("Mời bạn chọn một  chức năng bạn muốn sử dụng")
        if user_input =="1":
            add_event()
        elif user_input == "2":
            print_event()
        elif user_input == "3":
            count_down()
        elif user_input == "4":
            delete_event_user_choose()
        elif user_input == "0":
            print("Cảm ơn bạn đã sử dụng, Tạm biệt")
            break
        else:
            print("Giá trị nhập vào không hợp lệ, mời nhập lại")
            
            


if  __name__ =="__main__":
    main()
