N=[1,1,1,2,2,3]
k=2
res = {}
for i in N:
    res[i] = N.count(i)
lst = []
for i in range(k):
    maxmimumkey =max(res, key=res.get)
    lst.append(maxmimumkey)
    res.pop(maxmimumkey)
print(lst)