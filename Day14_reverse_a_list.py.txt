num_A = [1,2,3,4,56,78, 54]
start = 0
end = len(num_A) - 1
while start < end:
      temp = num_A[start]
      num_A[start] = num_A[end]
      num_A[end] = temp 
      start = start + 1
      end = end - 1
print (num_A)

#Output
#[54, 78, 56, 4, 3, 2, 1J ‎<This message was edited>
