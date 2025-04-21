def add_contact(contacts):
    name_input = input("Nhập tên liên hệ: ")
    name = name_input.lower()
    if name in contacts:
        print("Liên hệ đã tồn tại.")
        return
    phone = input("Nhập số điện thoại: ")
    email = input("Nhập email: ")
    contacts[name] = {
        'original_name': name_input,
        'phone': phone,
        'email': email
    }
    print("Đã thêm liên hệ.")


def view_contact(contacts):
    name = input("Nhập tên liên hệ cần xem: ").lower()
    if name in contacts:
        contact = contacts[name]
        print(f"{contact['original_name']} - SĐT: {contact['phone']}, Email: {contact['email']}")
    else:
        print("Không tìm thấy liên hệ.")


def edit_contact(contacts):
    name = input("Nhập tên liên hệ cần sửa: ").lower()
    if name in contacts:
        contact = contacts[name]
        phone = input("Nhập số điện thoại mới (nhấn Enter để bỏ qua): ")
        email = input("Nhập email mới (nhấn Enter để bỏ qua): ")
        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email
        print("Đã cập nhật liên hệ.")
    else:
        print("Không tìm thấy liên hệ.")


def delete_contact(contacts):
    name = input("Nhập tên liên hệ cần xóa: ").lower()
    if name in contacts:
        del contacts[name]
        print("Đã xóa liên hệ.")
    else:
        print("Không tìm thấy liên hệ.")


def display_all_contacts(contacts):
    if not contacts:
        print("Danh bạ trống.")
    else:
        print("Danh bạ hiện tại:")
        for contact in contacts.values():
            print(f"- {contact['original_name']} | SĐT: {contact['phone']}, Email: {contact['email']}")


def search_contact(contacts):
    keyword = input("Nhập số điện thoại hoặc email để tìm: ")
    found = False
    for contact in contacts.values():
        if keyword in contact['phone'] or keyword in contact['email']:
            print(f"Tìm thấy: {contact['original_name']} - SĐT: {contact['phone']}, Email: {contact['email']}")
            found = True
    if not found:
        print("Không tìm thấy liên hệ.")


def count_contacts(contacts):
    print(f"Tổng số liên hệ: {len(contacts)}")
