lst = [1,2,4,6,3,10,5]


for i in range(len(lst)-1):
    min_index = i
    for j in range(i+1,len(lst)-1):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i],lst[min_index] = lst[min_index],lst[i]
print(lst)


def recu(steps):
    
    if steps < 1: return
    print(steps)
    recu(steps-1)

