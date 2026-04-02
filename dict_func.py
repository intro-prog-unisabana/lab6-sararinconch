información = {
    "Name": "Diego",
    "Salary": 5000000,
    "Role": "Janitor",
    "Years at company": 9001,
    "Hours per week": 2
}
def employee_print(información):
    nombre = información.get("Name", "N/A")
    salario = información.get("Salary", "N/A" )
    rol = información.get("Role", "N/A" )
    print("Name:", nombre)
    print("Salary:", salario)
    print("Role:", rol)
    información.pop("Name", "N/A")
    información.pop("Salary", "N/A")
    información.pop("Role", "N/A")
    if not información:
        print("No other info!")
    else:
        for key, value in información.items():
            print(f"{key}: {value}")
