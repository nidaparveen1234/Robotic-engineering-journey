def palindrome_count(num,count):
    nums=num
    i=0
    while nums>0:
        digits=nums % 10
        i=i*10+digits
        nums = nums // 10
    if i==num:
        count=count+1
    return count


numbers = [121,1,2,3,123,432,12221,4566,12421,1345,7777]
count=0
for i in numbers:
      count =palindrome_count(i,count)
print(count)

# output
# 7
