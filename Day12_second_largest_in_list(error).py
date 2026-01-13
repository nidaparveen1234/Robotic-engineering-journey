numbers = [10,9,8,7]

max = numbers[0]
for i in numbers:
    if max <= i:
        second_max = max
        max = i
    elif max <=i:
    
        max = i
print(second_max)
print(max)

# output
# numbers = [1,2,3,4,5,-1,6,7,54,2]
# 7 
# 54
# numbers = [5,5,5]
# 5
# 5
