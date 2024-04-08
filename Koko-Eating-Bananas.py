import math
import sys


piles = [312884470] 
h = 968709470
# def require_time(piles,eatper):
#     totalhr=0
#     for i in piles:
#         totalhr += math.ceil(float(i)/float(eatper))
#     return totalhr
# ans = []
# for i in range(1,max(piles)):
#     totalhr = 0
#     totalhr=require_time(piles,i+1)
#     if totalhr <= h:
#         print(totalhr,"piles",i+1)
#         ans.append(i+1)

# print(min(ans))


low,high=1,max(piles)
ans = high

while low <= high:
    mid = (low + high)//2
    totalhr=0
    for i in piles:
        totalhr += math.ceil(i/mid)

    if totalhr <= h:
        ans = min(ans,mid)
        high = mid - 1
    else:
        low = mid +1


print(ans)