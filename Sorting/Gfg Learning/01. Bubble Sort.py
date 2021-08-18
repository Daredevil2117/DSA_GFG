''' In  bubble sort in every pass we swap adjecent elements if they are out of order and in every pass element at right gets fixed'''

def BubbleSort(arr):
    n=len(arr)
    swapped=False

    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True

        if swapped==False:
            break
    return arr

arr=[10,12,15,11,19,17,90,67,45,44,46]
print(BubbleSort(arr))

''' 
Stable: Yes
Time complexity in worst and avg case is O(n*n) and in best case is O(n)
Space Complexity O(1)
'''