list = [1,2,3,4]
start = 0
end = len(list)-1
k=2
rotation = 0
i=0
while rotation<=k:
    temp = list[start]
    while i<end:
        list[i]=list[i+1]
        i+=1
    list[end] = temp
    rotation+=1
print(list)

#output === [2, 3, 4, 2] ‎<This message was edited>
