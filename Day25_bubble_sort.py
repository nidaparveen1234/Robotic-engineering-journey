list = [9,9,9,9]
n=len(list)
i=0
j=0
for i in range(n):
    for j in range(n-1):
        if list[j]>=list[j+1]:
            temp = list[j+1]
            list[j+1] = list[j]
            list[j] = temp
print(list)

# output 
# [6,1,2,3,5,4]===[1, 2, 3, 4, 5, 6]
#[1,2,3,4,5,6]===[1, 2, 3, 4, 5, 6]
#[5,4,3,2,1]===[1, 2, 3, 4, 5]
#[5,4,9,3,2,1]===[1, 2, 3, 4, 5, 9]
#[5]====[5]
#[5,3]===[3,5]
#[9,9,9,9]===[9, 9, 9, 9]
