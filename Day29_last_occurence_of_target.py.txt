num_list =[1,2,2,2,3,4,6,7]
low =0
high = len(num_list) - 1
targt = 2
result = -1
while low <=high:
    mid = (low+high)//2
    if num_list[mid]< targt:
        high = mid - 1
    elif num_list[mid]> targt:
        low = mid + 1
    else:
        result = mid
        low = mid+1  # last occurence of target
if result == -1:
    print("it is not found",result)
else:
    print("it is found at index",result)

# [1,2,2,2,3,4,6,7]==== it is found at index 3
