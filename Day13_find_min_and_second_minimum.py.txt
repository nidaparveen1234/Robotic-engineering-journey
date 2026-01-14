numbers= [-1,-3,-43,3,3,2,2]
second_min = float('inf')
min = float("inf")
for i in numbers:
    if min>i:
        second_min= min
        min= i
    elif i > min and second_min>i:
        second_min=i
print("second minimum",second_min)
print("Minimum",min)


# output
#    numbers= [2,3,4,7,2,1,5,6,78]
# second minimum 2
# Minimum 1
#    numbers= [2,1,3,5]
# second minimum 2
# Minimum 1
#    numbers= [5,4,3,2,1]
# second minimum 2
# Minimum 1
#    numbers= [10,5]
# second minimum 10
# Minimum 5
#     numbers= [3,3,3]
# second minimum inf
# Minimum 3
#     numbers= [3,3,3,2,2]
# second minimum 3
# Minimum 2
#     numbers= [-1,-3,-43,3,3,2,2]
# second minimum -3
# Minimum -43
