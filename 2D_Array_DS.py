""" 
2D Array - DS 
Constraints: -9 <= arr[i][j] <= 9
             0 <= i,j <= 5
"""

def hourglassSum(arr):
    sum_biggest = -63 # constrain #1: if all elements are -9 then sum is -63
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr)-1): 
            s = sum((arr[i-1][j-1],arr[i-1][j],arr[i-1][j+1],arr[i][j],arr[i+1][j-1],
                        arr[i+1][j],arr[i+1][j+1]))           
            if s > sum_biggest:
                sum_biggest = s 
    return sum_biggest

# Test example
arr = [[1, 1, 1, 0, 0, 0],
       [0 ,1, 0, 0, 0, 0],
       [1 ,1, 1, 0, 0, 0],
       [0 ,0, 2, 4, 4, 0],
       [0 ,0, 0, 2, 0, 0],
       [0 ,0, 1, 2, 4, 0]]

hourglassSum(arr)
       