# Bài 4: Tính thưởng doanh thu

# ===== INPUT =====
salary = 15_000_000  # Lương cơ bản
sale = float(input("Nhập doanh thu thực tế: "))

# ===== PROCESS & OUTPUT =====
if sale > 100_000_000:
    luong_thuc_nhan = salary * 1.1
    print("Lương thực nhận:", luong_thuc_nhan)
elif sale >= 80_000_000 and sale <= 100_000_000:
    luong_thuc_nhan = salary
    print("Lương thực nhận:", luong_thuc_nhan)
elif sale >= 10_000_000 and sale < 80_000_000:
    luong_thuc_nhan = salary * 0.9
    print("Lương thực nhận:", luong_thuc_nhan)
else:
    print("Cần xử lý theo quy định doanh nghiệp")