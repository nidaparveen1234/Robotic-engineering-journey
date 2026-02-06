num_list =[1,2,34,5,3,4,3,2,2,1]
result_list =[]
for value in num_list:
    Found = False

    for item in result_list:
        if item[0] == value:
            item[1]+=1
            Found = True
    if not Found:
        result_list.append([value,1])

for key in result_list:
    print(key[0],"-",key[1])

#output == this question i worked so hard for me to get and  i got almost everything except for nested lists side
# and not found but i got some help from chatgpt and i was aable to reach here and i have more to learn in my journey 
# to be a better engineer
# 1 - 2
# 2 - 3
# 34 - 1
# 5 - 1
# 3 - 2
# 4 - 1
