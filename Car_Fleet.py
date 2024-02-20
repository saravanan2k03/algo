target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
target =12
# car=[[p,s]for p,s in zip(position,speed)] 
# stack=[]
# # print(car)
# # print(car[-1],car[-2],)
# for p,s in sorted(car,reverse=True):
#     stack.append(float((target-p)/s))

#     if len(stack) >=2 and stack[-1] <= stack[-2]:
#         print(stack)
#         print(stack[-1],stack[-2])
#         stack.pop()
    
# print(stack)



ans = 0
times = [float(target - p) / s for p, s in sorted(zip(position, speed),reverse=True)]
maxTime = 0 
print(times)
for time in times:
    print(time)
    if time > maxTime:
     print("maxTime",maxTime)
     maxTime = time
     ans += 1
print(ans)