# def missing_number(arr, n):
# arr = [1,2,3,5,6,8,9]
# n = 7

# sum1 = n*(n+1)/2
# sum2 = sum(arr)

# print(sum1 - sum2)



def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2
    
    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)
    
    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr
    
    return missing
 
# Example
print(missing_number([1,2,3,5,6,7,8,9], 9))  # Output: 5
# return mis



# print(missing_number([1,2,3,4,5,6,8,9],7))