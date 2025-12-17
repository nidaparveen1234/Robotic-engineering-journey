def is_prime(x):
    if x<=1:
        return False
    i=2
    while i*i<=x:
      if x%i==0:
       return False
      i+=1
    return True

x=int(input("enter the number"))
for i in range(2,x+1):
  if is_prime(i):
      print(i)
      

#output      
#enter the number9
#2
#3
#5
#7
