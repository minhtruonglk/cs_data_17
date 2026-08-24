# Bài 2: Kiểm tra số dương, âm hay bằng 0

# ===== INPUT =====
so = float(input("Nhập một số bất kỳ: "))

# ===== PROCESS & OUTPUT =====
if so > 0:
    print("Số dương")
elif so < 0:
    print("Số âm")
else:
    print("Bằng 0")