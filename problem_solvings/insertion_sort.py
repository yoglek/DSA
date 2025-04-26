### insertion sort 

## first we need to shift the elements in the sorted array if we find current element is less than last element in the sorted aray 
## This happens till the current element in the sorted array is less than the main element i 
## then insert the started key in the position were the while loop stopped

l = [2,3,0,1,4,5]

def insertion_sort(l):
    for i in range(1,len(l)):
        key = l[i]
        j = i-1
        while (j>=0 and l[j]>key):
            l[j+1] = l[j]
            j-=1
        l[j+1] = key
    return l

print(insertion_sort(l))

## Time complexity best case O(N) if th array is already sorted 
## worst case O(N)**2 since its has to go through the whole loop
## space complexity O(1) since these operations happening in place.





