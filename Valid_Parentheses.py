closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
s = "(]"
stack  = []
for c in s:
    if c in closeToOpen:
        if stack and stack[-1] == closeToOpen[c]:
            stack.pop()
        else:
            print(False)
    else:
        stack.append(c)
val = True if not stack else False
print(val)