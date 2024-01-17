import math

x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())

ans = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("{:.2f}".format(ans))




# 2 2
# 14 7