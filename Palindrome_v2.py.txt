x=int(input("enter the number"))
p=x
q=0
 
while p>0:
    mod =p%10
    q =q*10+mod
    p=p//10
    
print(q)
if(q==x):
    print("palimdrome")
else:
    print("not palindrome")
    

#output    
#enter the number121
#121
#palimdrome
