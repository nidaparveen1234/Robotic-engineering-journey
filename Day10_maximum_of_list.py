list =[-1,-2,-4,0]
max = list[0]
for i in list:
    if i >= max:
        max = i
    i+=1
print(max)

# output
# list = [12,2,3,24]===24
# list =[98,2,3,24]===98
# list =[98,12,1000,2,3,24]===1000
# list =[98,12,345,100,2,223,3,24]===345
# list =[-1,-2,-4]===-1
# list =[-1,-2,-4,0]===0
