num_list = [1,2,2,2,3,3,3,3,4,5]
low = 0
high = len(num_list) - 1
target = 3
result = -1
while low <= high:
    mid = (low+high)//2
    if num_list[mid]>target:
        high = mid - 1
    elif  num_list[mid]<target:
       low = mid+1
    else:
        result = mid
        high = mid - 1
if result == -1:
    print("found at index :",result)
else:
    print(" first occurence at index :",result)

# output
 #[1,2,2,2,3,4,5]=== first occurence at index : 1 ,when target == 2
 #[1,2,2,2,3,3,3,3,4,5]=== first occurence at index : 4 ,when target == 3
