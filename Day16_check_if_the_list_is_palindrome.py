num_list = [1,2,3,45,3,45,3,2,1]
start = 0
end = len(num_list) - 1
flag = 0
while start < end:
     if num_list[start] == num_list[end]:
          flag = 1
          start+=1
          end-=1
    
if flag==1:
    print("this is  palindrome")
else:
    print("this is not palindrome") ‎<This message was edited>
