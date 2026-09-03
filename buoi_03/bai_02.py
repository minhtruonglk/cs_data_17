# Bài 2: Phân loại số chẵn và số lẻ
# ===== INPUT =====
danh_sach = input("Nhập danh sách số nguyên, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, danh_sach.split(",")))

# ===== PROCESS & OUTPUT =====
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Danh sách số chẵn:", even_numbers)
print("Danh sách số lẻ:", odd_numbers)