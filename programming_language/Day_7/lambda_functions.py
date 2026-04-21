x = lambda y : 3*y
print(x(400))

stud=[
    {"name":"suhas","marks":50},
    {"name":"gautham","marks":40},
    {"name":"jayaam","marks":60}
]
stud.sort(key=lambda x:x["marks"])
print(stud)