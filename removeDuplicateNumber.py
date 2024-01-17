lst = [1, 1, 2, 2, 3, 4, 5]
un=[]
for i in range(len(lst)):
    if lst[i] not in un:
        un.append(lst[i])
print(un)