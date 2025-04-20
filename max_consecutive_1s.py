### Given binary array find the max consecutive 1s in the array

def get_max_consecutive_element(arr):
    current_count = 0
    max_count = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            current_count += 1
        else:
            current_count = 0

        max_count = max(max_count,current_count)
    return max_count

arr = [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(get_max_consecutive_element(arr))

## time complexity O(n)
## Space complexity, we have only the tho variables which requires constant amount of time O(1)

    





