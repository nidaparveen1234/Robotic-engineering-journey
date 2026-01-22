num_list = [1,2,3,4,5,6,7]
k = 10
if not num_list or k == 0: # this helps avoid crash rather than None it helps in [],0 etc
    print("try again")
else:
    start = 0
    end = len(num_list) -1
    
    for r in range(k):
        temp = num_list[end]
        for i in range(end,start,-1):
            num_list[i] = num_list[i-1]
            i-=1
        num_list[start] = temp
    print(num_list)

# output 
# when we are not considering k. this is output [5, 1, 2, 3, 4] but with k = [4, 1, 1, 2, 3]
# ohh now isee my confusion num_list[start] = temp was outside outer loop at first 
# so temp value was not getting stored now it is inside so eaxh temp vallue is getting stored
#when k = 2 , [4, 5, 1, 2, 3] when k = 3 , [3, 4, 5, 1, 2]
