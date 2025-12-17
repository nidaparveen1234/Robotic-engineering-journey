x =int(input("Enter the number"))

flag =0
i=2
if x<=1:
    print("not prime")
    
while i*i <= x:
    if x % i == 0:
     flag =1
     break
    i += 1
 
if flag==1:
    print("not prime")
else:
    print(" prime")
