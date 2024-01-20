lst = [-1, 0, 1]
setval = set(lst)
lenght = 1
longest = 0
print(setval)
for i in setval:
    if (i-1) not in setval:
        lenght=0
        while(i+lenght) in setval:
            print(i,"entered")
            lenght+=1
            longest = max(lenght,longest)
print(longest)


