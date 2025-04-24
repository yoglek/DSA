l = [2,3,1,4,5,6]

def bubble_sort(l):
    flag = True
    while flag:
        swap_count = 0
        for i in range(1, len(l)):
            if l[i] < l[i-1]:
                l[i] ,l[i-1] = l[i-1] ,l[i]
                swap_count+=1
        if swap_count == 0:
            flag = False
    return l

print(bubble_sort(l))

### Time complexity Worst Case O(N)2 best case when list is alreayd sorted then O(N)
### Space compaxity is constant as we update in the same list O(1)



