s = "rat"
t = "cat"
sdic = {}
tdic = {}
for i in s:
    sdic[i] = s.count(i)
for i in t:
    tdic[i] = t.count(i)
print(sdic)
print(tdic)
if sdic == tdic:
    print("There")

    
