lst = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target = 7
sumval = 0
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
            sumval = lst[i] + lst[j]
            if sumval == target:
                print(lst[i],lst[j],sumval)
            