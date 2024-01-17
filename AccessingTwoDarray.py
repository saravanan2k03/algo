import numpy as np

twoDArray = np.array([[1, 2, 3],[1,2,4]])
print(twoDArray)
print(len(twoDArray))
rowindex = len(twoDArray)
colindex = len(twoDArray)
print(twoDArray[1][2])
if rowindex >= len(twoDArray) or colindex >= len(twoDArray):
    print("incorrect row index")
