x =int(input("Enter the Number: "))
num=x
i=0
while num>0:
    t =num%10
    i=i*10+t
    num=num//10

print(i)
if i == x:
    print(f"{x} is palindrome")
else:
    print(f"{x} is not palindrome")

# Enter the Number123
# 321
# 123 is not palindrome
# Enter the Number12221
# 12221
# 12221 is palindrome
# Enter the Number: 1
# 1
# 1 is palindrome
# Enter the Number: 22
# 22
# 22 is palindrome
