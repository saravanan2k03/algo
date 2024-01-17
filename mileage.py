Ncars=int(input())
fueldata=[]
distancedata=[]
mileage=[]

for i in range(Ncars):
    Fuel,distance=map(str,input().split())
    fueldata.append(Fuel)
    distancedata.append(distance)
for i in range(Ncars):
    ans = int(distancedata[i])/int(fueldata[i])
    mileage.append(ans)
# mileage.sort()
position = mileage.index(max(mileage))
if position == len(mileage):
    print(position)
else:
    print(position+1) 

#     3
# 10 200
# 10 250
# 20 520