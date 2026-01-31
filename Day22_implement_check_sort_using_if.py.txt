new_list = [-9,-1,-4,0,3,4,3,2,2,1]
i=0
n = len(new_list)
start = 0
flag=0
while i<n-1:
    if new_list[i]>new_list[i+1]:
        flag = 1
        break  
    else:
        flag=0
    i+=1

if flag == 1:
    print("not sorted")
else:
    print("sorted")

# output
# [2,3,1,4]===not sorted
# [1,2,3,4,5]===sorted
# [1,2]=== sorted
# [1]=== sorted
# []== sorted
# [-9,-1,-4,0,3,4,3,2,2,1]=== not sorted
