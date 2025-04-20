## Give an list of stock prices for each day, find the best tiem to buy stocks 


def caluclate_max_profit(arr):
    profit_max = 0
    min_val_so_far = arr[0]
    for i in range(1,len(arr)):
        curr_profit = arr[i] - min_val_so_far
        profit_max = max(profit_max,curr_profit)
        min_val_so_far = min(min_val_so_far,arr[i])
    return profit_max

arr = [7,1,5,3,6,4]
print(caluclate_max_profit(arr))

## time complexity O(n)
## There are no data structures or extra arrays created that would take up additional space proportional to the input size.

# Space Complexity: O(1), because the algorithm only uses a constant amount of space for the variables.

# Summary:
# Time Complexity: O(n)

# Space Complexity: O(1)

    
