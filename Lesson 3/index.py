#my_set = {1,2,3}

#print(my_set)


#my_set = ([4,5,6])
#print(my_set)

#my_set = set()
#print(my_set)

#my_set = {1,1,2,2,3,3,4,2,1}
#print(my_set)

#set1 = {1,2,3}

#set2 = {4,5,6}


#union_method = set1.union(set2)
#print(union_method)


#union_operator = set1 | set2
#print("union of set1 and set2 using method:",union_method)
#print("union of set1 and set2 using method:",union_operator)


#intersection_method = set1.intersection(set2)


#intersection_operator = set1 & set2
#print("intersection of set1 and set2 using the intersection method",intersection_method)
#print("intersection of set1 and set2 using the intersection operator",intersection_operator)

#difference_method = set1.difference(set2)
#difference_operator = set1 - set2
#print("difference of set1 and set2 using the differnece method",difference_method)
#print("difference of set1 and set2 using the differnece operator",difference_operator)


#symetric_difference_method = set1.symetric_difference(set2)


#symetric_difference_operator = set1 ^ set2
#print("symetric difference of set1 and set2 using the symethric difference method",symetric_difference_method)
#print("symetric difference of set1 and set2 using the symethric difference operator",symetric_difference_operator)

my_set = {1,2,3}

my_set.add(7)

my_set.remove(3)

my_set.discard(8)

print(my_set)

my_set.clear()

print(my_set)

my_list = [1,1,1,2,3,4,2,3,4,5,6,]

unique_set = set(my_list)

unique_list = list(unique_set)
print(unique_list)

blertas_interest = {"music","movies"}
drilonis_interest = {"games","skiing","movies"}

common_interests = blertas_interest.intersection(drilonis_interest)
print(common_interests)

colors = {"red","blue","green"}
color = "red"
print(color in colors)