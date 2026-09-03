# Bài 3: Lọc các số lớn hơn hoặc bằng ngưỡng
# ===== INPUT =====
danh_sach = input("Nhập danh sách số nguyên, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, danh_sach.split(",")))
threshold = int(input("Nhập ngưỡng: "))

# ===== PROCESS & OUTPUT =====
result = []

for number in numbers:
    if number >= threshold:
        result.append(number)

print("Các số lớn hơn hoặc bằng ngưỡng:", result)