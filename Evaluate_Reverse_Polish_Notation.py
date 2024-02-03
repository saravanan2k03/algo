
tokens = ["18"]
stack = []
pattern = ['+', '-', '*','/']
c=0
for i in tokens:
    if i == "+":
        a=stack.pop()
        b=stack.pop()
        c=b+a
        stack.append(c)

    elif i == "-":
        a=stack.pop()
        b=stack.pop()
        c=b-a
        stack.append(c)
    elif i == "*":
        a=stack.pop()
        b=stack.pop()
        c=b*a
        stack.append(c)

    elif i == "/":
        a=int(stack.pop())
        b=int(stack.pop())
        c=int(b/a)
        stack.append(c)


print(stack[0])
