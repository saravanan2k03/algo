from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
d = defaultdict(list)

for i in strs:
    temp = "".join(sorted(i))
    d[temp].append(i)
print(list(d.values()))


for i in range(len(strs)):
    temp = "".join(sorted(strs[i]))
    print(temp)
    d[temp].append(strs[i])
print(list(d.values()))