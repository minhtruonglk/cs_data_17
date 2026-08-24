# Bài 1: Kiểm tra tuổi
# ===== INPUT =====
tuoi = int(input("Nhập tuổi: "))

# ===== PROCESS & OUTPUT =====
if tuoi < 0:
    print("Dữ liệu không hợp lệ")
elif tuoi < 18:
    print("Chưa đủ tuổi")
else:
    print("Đủ tuổi")