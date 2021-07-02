customer = {"name":"Ravi", "umur":25, "pekerjaan":"Programmer"}

name = customer["name"]
age = customer["umur"]
job = customer["pekerjaan"]

print(f"Hello My Name is {name} i am {age} years old, and im a {job}")


for key in customer:
    value = customer[key]
    print(f"{key} : {value}")