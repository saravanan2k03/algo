aList = [1,2,3,4,6,7]
for i in range(len(aList)):
    if len(aList) != 2:
        print(i)
        aList.pop(i)
        aList.pop()
print(aList)