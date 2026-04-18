fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']
fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']
fruits.insert(1, "kiwi")
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'cherry']
fruits.remove("orange")
print(fruits)  # Output: ['apple', 'kiwi', 'cherry']
fruits.pop()  # Removes the last item
print(fruits)  # Output: ['apple', 'kiwi']

fruits.pop(0)  # Removes the first item
print(fruits)  # Output: ['kiwi']
fruits.clear()
print(fruits)  # Output: []