num_list = [1,2,3,4,5,6]
start = 0
end = len(num_list)-1
k = 23
i = 0
rotation = k%end
while(rotation>0):
    temp = num_list[end]
    for i in range(end,start,-1):
        num_list[i] = num_list[i-1]
        i-=1
    num_list[start] = temp
    rotation-=1
print(num_list)

# output
# k = 2 === [5, 6, 1, 2, 3, 4]
# k = 10 ===[1, 2, 3, 4, 5, 6]
# k = 25 ===[1, 2, 3, 4, 5, 6]
# k = 23 ===[4, 5, 6, 1, 2, 3]
