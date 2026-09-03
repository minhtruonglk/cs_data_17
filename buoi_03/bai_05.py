# Bài 5: Tìm kiếm phần tử trong danh sách
# ===== INPUT =====
danh_sach = input("Nhập danh sách số nguyên, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, danh_sach.split(",")))
target = int(input("Nhập số cần tìm: "))

# ===== PROCESS & OUTPUT =====
positions = []

for i in range(len(numbers)):
    if numbers[i] == target:
        positions.append(i + 1)

if positions:
    print("Số", target, "xuất hiện tại vị trí:", positions)
else:
    print("Không tìm thấy số", target)