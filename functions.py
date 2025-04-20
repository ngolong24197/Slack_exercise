from datetime import datetime, timedelta
import os


FILE_NAME = "su_kien.txt"
DATE_FORMAT = "%Y-%m-%d %H:%M"


def create_event(line):
    parts = line.strip().split(" | ")
    name = parts[0]
    start_time = datetime.strptime(parts[1],DATE_FORMAT)
    duration = int(parts[2])
    repeat = parts[3]
    return {"name": name, "start": start_time, "duration" : duration, "repeat" : repeat}



def read_events():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME,"r", encoding="utf-8") as f:
        return[create_event(line) for line in f if line.strip()]
    

def write_event(event):
    with open(FILE_NAME,"a", encoding="utf-8") as f:
        line = f"{event["name"]} | {event["start"].strftime(DATE_FORMAT)} | {event["duration"]} | {event["repeat"]} \n" 
        f.write(line)
        
        
def check_conflit(new_event):
    for event in read_events():
        start1 = event["start"]
        end1 = start1 + timedelta(minutes=event["duration"])
        start2 = new_event["start"]
        end2 = start2 + timedelta(minutes=new_event["duration"])
        if max(start1,start2) < min(end1,end2):
            return event
    return None


def get_start_time(event):
    return event["start"]


def automation_event(days=30):
    all_event = []
    now =datetime.now()
    future = now +timedelta(days=days)
    for event in read_events():
        current = event["start"]
        while current <= future:
            if current >= now:
                all_event.append({
                    "name" : event["name"],
                    "start" : current,
                    "duration" : event["duration"],
                    "repeat" : event["repeat"]
                })
            if event["repeat"] == "weakly":
                current += timedelta(weeks=1)
            elif event["repeat"] == "monthly":
                try:
                    month = current.month + 1 if current.month <12 else 1
                    year = current.year if current.month <12 else current.year + 1
                    current = current.replace(year=year, month = month)
                except:
                    break
                
            else: 
                break
    return sorted(all_event, key = get_start_time)

def filter_event(mode = "all"):
    now = datetime.now()
    events = automation_event(30)
    if mode == "week":
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=7)
        return [e for e in events if start_of_week <= events["start"] < end_of_week]
    elif mode =="month":
        return [e for e in events if e["start"].month == now.month and e["start"].year == now.year]
    return events



def delete_event(index):
    events = read_events
    if 0 <= index <len(events):
        del events[index]
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for e in events:
                line = f"{e["name"] | {e["start"].strftime(DATE_FORMAT)} | {e["duration"]} | {e["repeat"]}} \n"
                
                
                

def calculate_remaining_time_event(event):
    now = datetime.now()
    delta = event["start"] - now 
    days = delta.day
    hours, remainder = divmod(delta.seconds, 3600)
    minutues = remainder//60
    
    return days,hours, minutues


def print_menu():
    print("\n📅 QUẢN LÝ SỰ KIỆN:")
    print("1. ➕ Thêm sự kiện mới")
    print("2. 📄 Xem danh sách sự kiện")
    print("3. ⏳ Thời gian còn lại đến sự kiện")
    print("4. ❌ Xoá sự kiện")
    print("0. 🔚 Thoát")
    
def add_event():
    name = input("Nhập tên sự kiện: ")
    start = input("Nhập thời gian bắt đầu theo định dạng( YYYY-MM-DD HH:MM: ")
    duration = int(input("Nhập thời lượng chương trình: "))
    repeat = input("Lặp lại? (None, Weekly, Monthly)")

    try:
        start_date = datetime.strptime(start,DATE_FORMAT)
        new_event = {"name": name, "start" : start_date, "duration" : duration, "repeat" : repeat}
        conflict_event = check_conflit(new_event)
        
        if conflict_event:
            print(f"Bạn đang có một sự kiện khác trong khoảng thời gian này : {conflict_event["name"]}, {conflict_event["start"]}")
            user_input = input("Bạn vãn muốn thêm mới sự kiện?")
            if user_input.lower() == 'y':
                print("Sự kiện đã được lưu")
                return write_event(new_event)
    except ValueError:
        print("Sai định dạng dữ liệu, mời bạn nhập lại")
                


def print_event():
    print("\nXem sự kiện:")
    print("1. Tất cả")
    print("2. Tuần này")
    print("3. Tháng này") 
    
    user_input = input("Lựa chọn của bạn: (1,2,3)")
    mode = "all"
    if user_input == "2":
        mode ="weekly"
    if user_input =="3":
        mode = "monthly"
    list_events = filter_event(mode)
    if not list_events:
        print("Bạn không có sự kiện nào trong khoảng thời gian trên")
        return None
    for i,e in enumerate(list_events):
        print(f"{i}. {e['name']} - Ngày {e['start'].strftime('%d/%m/%Y')}, Giờ {e['start'].strftime('%H:%M')} - {e['duration']} phút - {e['repeat']}")
        
        
def count_down():
    events = automation_event()
    if not events: 
        print("Bạn không có sự kiện nào trong khoảng thời gian trên")
        return None
    
    for i,e in enumerate(events, 1):
        print(f"{i}. {e['name']} - {e['start'].strftime('%d/%m/%Y %H:%M')}")
    try:
        index = int(input("Chọn số thứ tự đại diện cho một sự kiện mà bạn muốn kiểm tra thời gian còn lại: "))
        if 0<= index < len(events):
            days,hours, minutes = calculate_remaining_time_event(events[index])
            print(f"Thời gian còn lại tới khi bắt đầu sự kiện {events[index]["name"]} là {days} ngày, {hours} giờ, {minutes} phút ")
        else:
            print("Giá trị nhập vào không chính xác")
    except:
        print("Giá trị nhập vào không chính xác")
        
    
def delete_event_user_choose():
    events = read_events()
    if not events:
        print("Bạn không có sự kiện nào trong khoảng thời gian trên")
        return None   
    for i,e in enumerate(events, 1):
        print(f"{i}. {e['name']} - {e['start'].strftime('%d/%m/%Y %H:%M')}")
    try:
        index = int(input("Chọn số thứ tự đại diện cho một sự kiện mà bạn muốn xóa: ")) -1 
        if 0<= index < len(events): 
            delete_event(index)
            print("Đã xóa thành công")
    except ValueError:
        print("Giá trị nhập vào không hợp lệ")
        