#for tuples or list elements
def pro(*a):
    print(sum(a))

pro(1,2,3,4,5)

#for dictoionary use 2 stars (**)
def pro2(**b):
    for key,value in b.items():
        print(f"{key}-{value}")

pro2(name="suhas",age=21,Placed="No")
