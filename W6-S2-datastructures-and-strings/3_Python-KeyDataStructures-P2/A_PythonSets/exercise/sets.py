

set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

union_set = set1.union(set2)

intersection_set = set1.intersection(set2)

print("Intersetion of set1 & set2 ", intersection_set)

difference_set = set1.difference(set2)

print("Difference of set1 and set2: ", difference_set)

set1.add(9)

print("Added 9 to set 1 ", set1)

set1.remove(9)

print("Removed 9 from set1: ", set1)


set2.remove(11)

print(set2)

print(set1)
print(set2)