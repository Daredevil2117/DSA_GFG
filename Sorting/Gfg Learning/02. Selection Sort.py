''' In selection sort in each pass we find min element and replaces with element in place of it
It maintains two subarrays at a time sorted one and unsorted one
'''

def SelectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr

arr=[10,12,15,11,19,17,90,67,45,44,46]
print(SelectionSort(arr))

'''
Time complexity in all cases O(n*n)
Space Complexity: O(1)
Advantage: Since it takes maximum of n swaps so it is used in memory write operations(EPROM).
'''