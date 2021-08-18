'''
. The array is virtually split into a sorted and an unsorted part.
 Values from the unsorted part are picked and placed at the correct position in the sorted part.
'''

def InsertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=[10,12,15,11,19,17,90,67,45,44,46]
print(InsertionSort(arr))

'''
Time Complexity in Best Case when array is already sorted: O(n)
Time Complexity in avg and worst case: O(n*n)
Tim Sort like function of python sort() it uses merge sort when array is large
 and switches to insertion sort when array is small
'''
