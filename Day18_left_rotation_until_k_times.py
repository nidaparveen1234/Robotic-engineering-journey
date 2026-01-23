list = [1,2,3,4,5,6]
start = 0
end=len(list)-1
rotation = 0
k=3
while rotation< k:
    temp = list[start]
    i=start
    for i in range(start,end,1):
        list[i]=list[i+1]
        i+=1
    list[end]=temp
    rotation+=1
print(list)

# output
# k=2 [3, 4, 5, 1, 2]
#k = 3 [4, 5, 6, 1, 2, 3]
