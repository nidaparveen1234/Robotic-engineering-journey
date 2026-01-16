nums = [1,23,45,54,22,22,22,11]
start = 0
end = len(nums) -1
while start < end:
    temp = nums[start]
    nums [start] = nums [end]
    nums [end] = temp
    start +=1
    end --1
print(nums)

#Output
#nums = [1,23,45,54,22,22,22,11]
#[11, 22, 22, 22, 54, 45, 23, 1]
#nums = [ ]
#[ ]
#nums=[1]
#[1] ‎<This message was edited>
