myList2D= [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
sumlist = []
mid = len(myList2D) // 2
print(mid,len(myList2D))
for i,val in enumerate(myList2D):
    print(val)
    if i != mid:
        sumlist.append(val[0])
        sumlist.append(val[-1])
    else:
        secondmid = len(val) // 2
        sumlist.append(val[secondmid])

print(sum(sumlist))



def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0
 
    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]
 
    return total