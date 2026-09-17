# Bài 5: Tổng lương theo phòng ban
# ===== INPUT =====
employees = {
    "name": ["An", "Bình", "Chi", "Dũng"],
    "department": ["IT", "IT", "HR", "Finance"],
    "salary": [2000, 3000, 1500, 2500]
}

salary_by_department = {}

# ===== PROCESS & OUTPUT =====
for i in range(len(employees["department"])):
    department = employees["department"][i]
    salary = employees["salary"][i]

    if department in salary_by_department:
        salary_by_department[department] += salary
    else:
        salary_by_department[department] = salary

print(salary_by_department)