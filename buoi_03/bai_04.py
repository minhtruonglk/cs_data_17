# Bài 4: Sắp xếp danh sách theo thứ tự tăng dần
# ===== INPUT =====
danh_sach = input("Nhập danh sách số nguyên, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, danh_sach.split(",")))

# ===== PROCESS & OUTPUT =====
for i in range(len(numbers) - 1):
    min_index = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("Danh sách sau khi sắp xếp:", numbers)