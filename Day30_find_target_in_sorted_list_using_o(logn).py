	new_list = [5,5,5,5,5]
low =0
high =len(new_list)-1
target =5
frst_occ=-1
while low<=high:
    mid= (low+high)//2
    if new_list[mid]>target:
        high=mid-1
    elif new_list[mid]<target:
        low = mid+1
    else:
        frst_occ= mid
        high = mid -1
low =0
high =len(new_list)-1
lst_occ = -1
while low<=high:
    mid= (low+high)//2
    if new_list[mid]>target:
        high=mid-1
    elif new_list[mid]<target:
        low = mid+1
    else:
        lst_occ = mid
        low = mid +1
        
freq = lst_occ - frst_occ +1
print("the freq is",freq)
# [1,2,2,2,3,4]====the freq is 3
#  [5,5,5,5,5]====the freq is 5
