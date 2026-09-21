# Bài 3: Hàm xóa trường thông tin
# ===== INPUT =====
def xoa_truong(data, field):
    if field in data:
        return data.pop(field)
    else:
        return "Trường thông tin không tồn tại"


employee = {
    "name": "An",
    "department": "IT",
    "salary": 2000
}

# ===== PROCESS & OUTPUT =====
print(xoa_truong(employee, "department"))
print(xoa_truong(employee, "phone"))