set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}

intersection_set = set1 & set2  # Output: {3}

difference_set = set1 - set2  # Output: {1, 2}

sym_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5}

print(union_set)
print(intersection_set)
print(difference_set)
print(sym_diff_set)
