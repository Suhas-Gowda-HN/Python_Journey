fruits_set = ["apple", "banana", "cherry"]

fruits_set.add("orange")
print(fruits_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}

fruits_set.remove("banana")
print(fruits_set)  # Output: {'apple', 'cherry'}

fruits_set.discard("banana")  # No error if "banana" is not in the set

fruits_set.pop()#removes random element

fruits_set.clear()