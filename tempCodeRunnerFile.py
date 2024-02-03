stack = []
res=[]
s = "()[]"
pattern = {"(":")","[":"]","{":"}"}
for i in s:
    stack.append(i)

print(stack)
l=0
r=len(stack)-1
print(r)
print(stack[r])
while l < r:
    r=len(stack)-1
    stack[r]
    if pattern.get(str(stack[l])) == stack[r]:
        res.append(True)
        stack.pop(l)
        stack.pop(r)
    else:
        stack.pop(l)
        res.append(False)
print(res)