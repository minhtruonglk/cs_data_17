# Bài 5: Đăng nhập đơn giản

# ===== INPUT =====
USERNAME = "truongnm"
PASSWORD = "Truong@135790"

input_username = input("Nhập username: ")
input_password = input("Nhập password: ")

# ===== PROCESS & OUTPUT =====
if input_username == USERNAME and input_password == PASSWORD:
    print("Đăng nhập thành công")
else:
    print("Đăng nhập thất bại")