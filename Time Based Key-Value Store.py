store = {}
store["saro"]=[]
store["saro"].append(["bar", 1])
store["saro"].append(["bar2", 4])
store["saro"].append(["bar2", 6])
store["saro"].append(["bar2", 7])
store["saro"].append(["bar3", 8])
value = store.get("saro",[])
print(value)
res = ""
timestamp=2
low,high=0,len(value)-1
while low <= high:
    mid= (low+high)//2
    if value[mid][1] == timestamp:
        res = value[mid][0]
        print("finded value: " + res)
    if value[mid][1] <= timestamp:
        res = value[mid][0]
        low = mid+1
    else:
        high = mid - 1

print(res)
        
