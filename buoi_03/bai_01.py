# Bài 1: Tìm số lớn thứ hai
# ===== INPUT =====
danh_sach = input("Nhập danh sách số nguyên, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, danh_sach.split(",")))

# ===== PROCESS & OUTPUT =====
largest = None
second_largest = None

for number in numbers:
    if largest is None or number > largest:
        second_largest = largest
        largest = number
    elif number != largest and (second_largest is None or number > second_largest):
        second_largest = number

if second_largest is None:
    print("Không có số lớn thứ hai")
else:
    print("Số lớn thứ hai:", second_largest)