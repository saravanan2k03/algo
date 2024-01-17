# import math
# x1,y1=2,2
# x2,y2=14,7
# x=x2-x1
# y=y2-y1
# val = x^2+y^2
# val = float(val)
# val = math.sqrt(val)
# print(val)


aList = [1,2,3,4,6,7]
#minus 1 because the first element is index 0
middleIndex = (len(aList)-1)
# print (middleIndex)
# print (aList[int(middleIndex)])
aList = [1,2,3,4,6,7]
for i in range(len(aList)):
    if len(aList) != 2:
        print(i)
        aList.pop(i)
        aList.pop()
print(aList)