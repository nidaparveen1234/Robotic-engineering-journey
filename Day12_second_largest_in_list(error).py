numbers = [2,1,3,5]
second_max= float('inf')
max = numbers[0]
for i in numbers:
    if i > max:
        second_max = max
        max = i
    elif i < max and i > second_max:
        second_max = i
print(second_max)
print(max)

# output
# numbers = [10,9,8,7]
# 9
# 10
# numbers = [1,2,3,4,5,-1,6,7,54,2]
# 7 
# 54
# numbers = [5,5,5]
# 5
# 5
# numbers = [1,2]
# 1
# 2
# numbers = [2,1,3,5]
# 3
# 5
