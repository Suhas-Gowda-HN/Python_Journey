def table():
    a = "suhas"
#print(a) gives error because its local variable

b = "gowda"# this is a global variable
def sos():
    a = "suhas"+b

sos()

