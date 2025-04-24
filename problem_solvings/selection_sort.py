l = [2,3,1,4,5,0]

def selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_index]:
                 min_index = j
        
        l[i], l[min_index] = l[min_index], l[i]
    return l

print(selection_sort(l))


### Time complexity worst case O(N)2 and 
## best case O(n)2 becase even we need to iterate the entire array for all the element even for the sorted array
## space complexity sorting in place so O(1)