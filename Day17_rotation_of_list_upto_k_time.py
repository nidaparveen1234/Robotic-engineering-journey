lst = ['A', 'B', 'C', 'D', 'E']
k = 2

start = 0
end = len(lst) - 1

for r in range(k):
    temp = lst[end]            

    for i in range(end, start, -1):
        lst[i] = lst[i-1]

    lst[start] = temp            

print(lst)
