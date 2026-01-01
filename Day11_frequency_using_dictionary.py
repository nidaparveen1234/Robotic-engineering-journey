numbers = [1,2,3,4,5,1,1,3,3,2,5,5]
freq = {}
for i in numbers:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
    
print("final answer")
for key in freq:
    print(key ,"-", freq[key])

# output
# final answer
# 1 - 3
# 2 - 2
# 3 - 3
# 4 - 1
# 5 - 3
