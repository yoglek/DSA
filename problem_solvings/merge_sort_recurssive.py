### merge sort inplace using the merge sort theory 
### This approach uses the divide and conquer technique.
# ## we are using recurssive method to perform merge operation 
# 
# 
# 

a = [6, 7, 8, 9, 10, 11,0, 1, 2, 3,4,5]

def merge_Sort(left,right):
    if left<right:
        mid = (left+right)//2
        merge_Sort(left,mid)
        merge_Sort(mid + 1,right)
        merge(left, mid,right)

def merge(start, mid, end):
    i = start
    j = mid+1
    k = 0
    c = [0] * (end - start+1)

    while (i<=mid or j<=end):
        if (i<=mid and j<=end):
            if a[i]<=a[j]:
                c[k] = a[i]
                i+=1
            else:
                c[k] = a[j]
                j+=1
        elif(i<=mid):
            c[k] = a[i]
            i+=1
        else:
            c[k] = a[j]
            j+=1        
        k+=1

    for i in range(len(c)):
        a[start+i] = c[i]


merge_Sort(0,len(a)-1)       
print(a)      



## time complexity O(N Log N) since N/2 recurssives
## space complexity O(N)

