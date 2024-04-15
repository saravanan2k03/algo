
prices = [2,4,1]
maxProfit = 0

left = 0
for right in range(1,len(prices)):
    if prices[left] < prices[right]:
        maxProfit = max(maxProfit,(prices[right]-prices[left]))
    else:
        left = right



print(maxProfit)

