### Merge sort 
# Sort two sorted arrays, using merge sort technique 
# 1. Give two array a and b, these two are already sorted 
# Thne we need to take element from each and compare 
# and insert into a new array at the next position 
# 
# 

a = [1,3,5,6,8,9]  
b = [0,2,4,7,10,11]


def merge_sort_sorted_array(a,b):
    n = len(a)
    m = len(b)
    c = [1] * (n+m)
    i,j,k = 0,0,0
    while (i<n or j<m):
        if (i<n and j<m):
            if a[i]<=b[j]:
                c[k] = a[i]
                i+=1
            else:
                c[k] = b[j]
                j+=1
            k+=1
        elif(i<n):
            c[k] = a[i]
            i+=1
            k+=1
        else:
            c[k] = b[j]
            j+=1
            k+=1
    return c


print(merge_sort_sorted_array(a,b))
## Time complexity O(N+M) --> O(N) which is linear complexity
## space complexity we are creating a new list which is size O(n+m) --> O(N) linear complexity




