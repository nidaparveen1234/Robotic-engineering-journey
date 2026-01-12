numbers = [1,2,3,56,56,32,1,2,3,4,5,6,7,1,1,56]
freq ={}
for i in numbers:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for key in freq:
    print(key,"->",freq[key])

max_key = None
max_value = 0
for key,value in freq.items():
    if value >= max_value:
        max_value = value
        max_key = key
print("Maximum value")
print(max_key,"->",max_value)


# output
# 1 -> 4
# 2 -> 2
# 3 -> 2
# 56 -> 3
# 32 -> 1
# 4 -> 1
# 5 -> 1
# 6 -> 1
# 7 -> 1
# Maximum value
# 1 -> 4
