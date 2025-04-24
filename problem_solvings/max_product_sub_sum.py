### maximum sum sub array problem

arr = [1,2,-3,4,5,6]

### We can use the kadane's algorithm 

def max_sum_subarray(arr):
    max_sum = arr[0]
    curr_sum = arr[0]

    for i in range(1,len(arr)):
        if curr_sum<0:
            curr_sum = 0
        curr_sum +=arr[i]
        max_sum = max(max_sum,curr_sum)
    return max_sum
print(max_sum_subarray(arr))

## time complexity linear so O(N)
## Space Complexity O(1) bcs its constant time


