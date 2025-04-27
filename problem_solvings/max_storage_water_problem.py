### two pointer problem 
### given the list of heighets in an array find the maximum points we can store the water 
### water problem - we can use the two pointer appraoch 
## area formula height * width

heights = [1,8,6,2,5,4,8,3,7]
def get_maximum_volume(heights):
    i= 0
    j = len(heights) - 1
    max_volume = 0
    while i<j:
        area = min(heights[i],heights[j]) * (j-i)
        max_volume = max(max_volume,area)

        if heights[i] < heights[j]:
            i+=1
        else:
            j-=1
    return max_volume


print(get_maximum_volume(heights))


## Time Complexity O(N) - Linear time 
## Space Complexity O(1) -  Constant time

