nums =[23,45,67,89,54,32,34,43]
start = 1
end = 4
while start < end:
     temp = nums [start]
     nums [start]= nums [end]
     nums [end] = temp 
     start +=1
     end --1
print (nums)

#Output
# [23, 54, 89, 67, 45, 32, 34, 43]
