'''
Merge sort works upon divide and conquer rule divides array  into two halves the merges them
'''

def MergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        MergeSort(l)                           # Breaking the left part
        MergeSort(r)                           # Breaking the right part
        i=j=k=0

        while(i<len(l) and j<len(r)):        # Combining both part using merge function
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
                k+=1
            else:
               arr[k]=r[j]
               j+=1
               k+=1
        while(i<len(l)):
            arr[k]=l[i]
            i+=1
            k+=1
        while(j<len(r)):
            arr[k]=r[j]
            j+=1
            k+=1
def printarray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
arr=[8,6,1,2,3,4,5,3,4,5,9,8]
MergeSort(arr)
printarray(arr)

'''
Time Complexity: Number of levels * work done at each level=O(n)*ceil(O(logn)) == O(nlogn)
Space Complexity: O(n)  bcz extra space allocated gets deallocate once that level merges.
'''