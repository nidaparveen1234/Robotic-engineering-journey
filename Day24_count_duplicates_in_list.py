list = [1,2,3,4,4,32,1,3,4,5,32,1,1]
result =[]
count = 0
for value in list:
    for item in result:
        if item[0] in result:
            item[1]+=1
        else:
            result.append([value][1])

for key in result:
    print(key[0],"-",key[1])

    #error
