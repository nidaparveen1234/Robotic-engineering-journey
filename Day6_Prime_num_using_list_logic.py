def isprime(num):
     if num<=1:
        return False
     
     i =2
     while i*i<=num:
         if num%i==0:
             return False
         i+=1
     return True

numbers = [1,2,3,4,5,6,7,8,9,12,98,15,-5,0,19,49,121,25,97]
for i in numbers:
    if isprime(i):
        print(i,end=" ")

# output
#   2 3 5 7 19 97
