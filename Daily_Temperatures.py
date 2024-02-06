temperatures = [73,74,75,71,69,72,76,73]
stack = []
res=[0]*len(temperatures)

# for i in range(len(temperatures)):
#     for j in range(i+1,len(temperatures)):
#         if temperatures[j] > temperatures[i]:
#             stack[i] = j-i
#             break
# print(stack)        

for i,temp in enumerate(temperatures):
    while stack and temp > stack[-1][0]:
        stacktemp,stackindex=stack.pop()
        res[stackindex] = (i-stackindex)        
    stack.append([temp,i])
print(res)