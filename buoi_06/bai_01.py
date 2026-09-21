# Bài 1: Hồ sơ sản phẩm
# ===== INPUT =====
product = {
    "id": 1,
    "name": "Laptop",
    "price": 15000000,
    "quantity": 10
}

# ===== PROCESS & OUTPUT =====
print("Tên sản phẩm:", product["name"])

product["price"] = 16000000

product["category"] = "Điện tử"

del product["quantity"]

print("Product:", product)