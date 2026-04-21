def default(boy,girl="random girl"):
    print(f"{boy} likes a {girl}")

default("paul","criste")
default("paul")

def addi(a,b):
    return (a+b)

c = addi(2,4) + 10
d = 10+addi(5,6)
print(c)
print(d)