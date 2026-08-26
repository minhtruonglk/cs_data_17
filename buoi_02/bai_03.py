# Bài 3: Xếp loại điểm

# ===== INPUT =====
diem = float(input("Nhập điểm: "))

# ===== PROCESS & OUTPUT =====
if diem < 0 or diem > 10:
    print("Điểm không hợp lệ")
elif diem >= 9:
    print("Xuất sắc")
elif diem >= 8:
    print("Giỏi")
elif diem >= 6.5:
    print("Khá")
elif diem >= 5:
    print("Trung bình")
else:
    print("Yếu")