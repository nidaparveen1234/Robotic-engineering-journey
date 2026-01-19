num_list = [7,7,1,3,4,2,2,4,2]
start = 0
end = len(num_list) - 1
flag = 0
while start < end:
     if num_list[start] != num_list[end]:
          flag = 1
          break
          start+=1
          end-=1
    
if flag==1:
    print("this is not palindrome")
else:
    print("this is  palindrome")

#Output
#num_list = [1,2,3,45,3,45,3,2,1]===this is palindrome
#num_list = [1,2,3,45,3,3,2,1]===this is not palindrome
