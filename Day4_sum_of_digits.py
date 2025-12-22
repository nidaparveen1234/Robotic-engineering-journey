x=int(input("Enter the Number"))
sum=0
i=x

while x>0:
    i=x%10
    sum+=i
    x=x//10

print(sum)
# Enter the Number098
# 17
# Enter the Number123
# 6
