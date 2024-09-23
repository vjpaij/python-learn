breakfast = ["Dosa", "Idli", "Upma", "Puri"]
lunch = ["Biriyani", "Naan"]
dinner = ["Salad", "Fried Rice", "Roti"]

menu = [["Dosa", "Idli", "Upma", "Puri"], ["Salad", "Fried Rice", "Roti"], ["Biriyani", "Naan"] ]

print(menu[1])
print(menu[1][2])

menus= {"breakfast" : ["Dosa", "Idli", "Upma", "Puri"],
        "lunch" : ["Salad", "Fried Rice", "Roti"],
        "dinner" : ["Biriyani", "Naan"]}

print("Breakfast Menu : \t", menus["breakfast"])
print("Lunch Menu : \t", menus["lunch"])
print("Dinner Menu : \t", menus["dinner"])

for name,food in menus.items():
    print(name, ":", food)

for x in menus:
    print(menus.get(x)) 

employee = {"Name" : "Gabriel Fischer",
            "ID" : 223344,
            "Designation" : "Vice-President"}

print(employee.get('Name'), "works for Wipro as", employee.get('Designation'))
