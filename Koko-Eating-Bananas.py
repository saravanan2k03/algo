import math


piles = [3,6,7,11]
h = 8

low = 0
high = max(piles)
ans=high
totalhr = 0
while low <= high:
    mid = (low + high)//2
    totalhr = 0
    for i in piles:
        totalhr += math.ceil(i/mid)
    if totalhr <= h:
        ans = mid
        high = mid-1
    else:
        low = mid+1

print(ans)
        
        
