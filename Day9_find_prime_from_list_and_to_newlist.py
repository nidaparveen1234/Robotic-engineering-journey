def is_prime(x):
    if x<=0:
        return False
    i=2
    while i*i<=x:
        if x%i==0:
            return False
        i+=1
    return True

listA=[1,2,3,4,5,6,7,8,9,0,12,24,15,98,17]
listB=[]
for i in listA:
    if is_prime(i):
        listB.append(i)
print(listB)

# output
# [1, 2, 3, 5, 7, 17]
