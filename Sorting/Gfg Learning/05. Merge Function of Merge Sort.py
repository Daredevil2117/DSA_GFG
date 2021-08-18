'''
Given three indices low mid and high and an array elements in array from low to mid are sorted
and mid+1 to high are sorted. sort these elements from low to high together.
'''
def MergeFunction(arr,low,mid,high):
    n1=mid-low+1;n2=high-mid               # Counting number of sorted elements in both the part
    left=[]
    right=[]
    for i in range(n1):
        left.append(arr[low+i])
    for j in range(n2):
        right.append(arr[mid+1+j])

    i=0;j=0;k=low
    while(i<n1 and j<n2):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
            k+=1
        else:
            arr[k]=right[j]
            j+=1
            k+=1
    while(i<n1):
        arr[k]=left[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k]=right[j]
        j+=1
        k+=1
    return arr

arr=[8,6,1,2,3,4,5,3,4,5,9,8]    # array is sorted from 2 to 6 and then 7 to 9 so low=2 mid=6 high=9
print(MergeFunction(arr,2,6,9))

'''
Time Complexity: O(n)
Space Complexity:O(n)  # as total size of new arrays left + right is n
'''