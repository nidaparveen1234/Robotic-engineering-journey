num_list = [1,2,3,4,5]
start = 0
end = len(num_list)-1
k=3
rotation = 0
while rotation < k:
    temp = num_list[end]
    i = end
    while i>start:
        num_list[i] = num_list[i-1]
        i-=1
    num_list[start] = temp
    rotation+=1
print(num_list)

# output
# num_list = [1,2,3,4,5] ==== [4, 5, 1, 2, 3]
# num_list = [1,2,3,4,5] === [3, 4, 5, 1, 2]
