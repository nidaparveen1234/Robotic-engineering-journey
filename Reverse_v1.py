x=int(input("enter the num"))

p= 0
q = x
while q>0:
     t=q%10
     p =p*10+t
     q=q//10
if p==x:
    print("palindrome")
else:
   print("not palindrome") 
   
print(p)
