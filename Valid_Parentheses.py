s = "()"
print(len(s))
stack = []
for i in range(len(s)):
    print(s[i])
    stack.append(s[i])
    if len(stack) > 1:
        print(stack)
        stval1 = stack[i-1]
        stval = stack[i]
        print(stval,stval1)
        if stack[i] == stack[i-1]:
            print("Stack")