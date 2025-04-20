## product of an array given except self

def product_array_except_self(arr): 
    left_arr = [1] * len(arr)
    right_arr = [1] * len(arr)

    for i in range(1,len(arr)):
        left_arr[i] = left_arr[i-1] * arr[i-1]
    for i in range(len(arr)-2,-1,-1):
        right_arr[i] = right_arr[i+1] * arr[i+1]

    return [i*k for i,k in zip(left_arr,right_arr)]


arr = [5,2,3,4]
print(product_array_except_self(arr))


## Time complexity O(N)
## Space complexity, we have only the tho variables which requires constant amount of time O(N)

    


