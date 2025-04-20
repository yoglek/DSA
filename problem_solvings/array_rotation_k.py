### rotate an array k times 

def rotate_array_k_stesp(arr,k):
    n = len(arr)
    k = k % n

    ### revese the entire array
    ### reverse the first k elements
    ### reverse the first last n-k elements 

    def reverse(test_arr,s,e):
        while s<e:
            test_arr[s], test_arr[e] = test_arr[e], test_arr[s]
            s+=1
            e-=1
        return test_arr

    arr = reverse(arr,0,n-1)
    arr = reverse(arr,0,k-1)
    arr = reverse(arr,k,n-1)

    return arr
arr = [1,2,3,4,5,6,7]
k = 22
print(rotate_array_k_stesp(arr,k))


## time complexity is O(N)
## Space complexity O(1)
