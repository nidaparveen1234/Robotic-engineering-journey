num_list = [1,2]
size_of_list = len(num_list)
i=0
flag = 0
for i in range(0,size_of_list-1):
    j = i+1
    for j in range(j,size_of_list):
        if num_list[i] == num_list[j]:
            flag = 1
            break
        else:
            j+=1
    i+=1

if flag == 1:
    print("duplica")
else:
    print("not duplica")

# output
# [1,2,3,4,5,6,1]===duplica
#[1,2,3,4,5,6]===not duplica
#[1,2,3,4,4,5,6,7,1,2,3,8]===duplica
#[1]===not duplica
#[]===not duplica
#[1,2]===not duplica
