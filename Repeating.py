N = list(map(int,input().split()))
N.sort()
res ={}
maxmimumduplicates =[]
for i in N:
    res[i] = N.count(i)
print(res)
maxmimumkey =max(res, key=res.get)
print(maxmimumkey)
print('maxmimum',res[maxmimumkey])
maxmimum = res[maxmimumkey]
for key,value in res.items():
    print(res.values())
    if maxmimum == value:
        maxmimumduplicates.append(key)
print(min(maxmimumduplicates))









# 5 10 5 15 20 25 15 18 15