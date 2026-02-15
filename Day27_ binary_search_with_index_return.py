num_list = [1,2,3,4,7,9,12,15]
low = 0
high = len(num_list)-1
target = 7
result = -1

while low<=high:
    mid = (low +high)//2
    if num_list[mid]>target:
        high = mid-1
    elif num_list[mid]<target:
        low = mid +1
    elif num_list[mid]==target:
        result = mid
        break

print("the result is found at index",result)
#the result is found at index 4
