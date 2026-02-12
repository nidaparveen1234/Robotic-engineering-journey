num_list =[1,3]
low =0
high =len(num_list)-1
target =2
found = False
while(low<=high):
    mid =(low+high)//2
    if num_list[mid] == target:
        found = True
        break
    elif num_list[mid] > target:
        high = mid - 1
    elif num_list[mid] < target:
        low = mid + 1
if not found:
    print("not found")
else:
    print("found")

# output
# [1,2,3,4,5,6]===found
# [1,2,2,3,4,5,6]===found
#[1,3,4,5,6]===not found
#[1,3]===not found
