l = [1,2,3,4,5,6,7,8]
print(l)

#dl = [expression for item in list]
dl = [item*2 for item in l]
print(dl)

#list comprehension using if statments
pl = [x**2 for x in l if x%2==0]
print(pl)

