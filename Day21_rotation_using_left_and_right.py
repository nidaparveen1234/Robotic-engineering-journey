def right_rotation(rotation,arr):
    start = 0
    end = len(new_list)-1
    while rotation>0:
        temp =arr[end]
        for i in range(end,start,-1):
            arr[i]=arr[i-1]
        arr[start]=temp
        rotation-=1
    print(arr)


def left_rotation(rotation):
    new_list = [1,2,3,4,5,6,7]
    start = 0
    end = len(new_list)-1
    while rotation>0:
        temp = new_list[start]
        i=start
        for i in range(start,end):
            new_list[i]=new_list[i+1]
        new_list[end]=temp
        rotation-=1
    print(new_list)


new_list = [1,2,3,4,5,6,7]
start = 0
end = len(new_list)-1
k=3
rotation = k % len(new_list)
right_rotation(rotation,new_list)
left_rotation(rotation)

# output
# if i don't put an list inside the function it would give me this 
# [5, 6, 7, 1, 2, 3, 4]
#[1, 2, 3, 4, 5, 6, 7]

# but i put it inside function so it should on two different function so 
# we get ides of how left and right rotation works
# [5, 6, 7, 1, 2, 3, 4]
# [4, 5, 6, 7, 1, 2, 3]
