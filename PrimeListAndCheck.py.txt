def isprime(x):
    if x<=1:
        return False
    
    i =2
    while(i*i<=x):
        if x%i==0:
            return False
        i+=1
    return True
 
x = int(input("Enter the number"))
if isprime(x):
    print("prime ")
else:
    print("not prime")

for i in range(2,x+1):
    if isprime(i):
        print(i)

# Enter the number20
# not prime
# 2
# 3
# 7
# 11
# 13
# 17
# 19

# Enter the number7
# prime 
# 2
# 3
# 5
# 7
