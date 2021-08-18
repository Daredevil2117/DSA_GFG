''' Given two sorted arrays print all the the elements of the arrays in sorted order'''

def MergeArrays(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    i=0;j=0
    while(i<m and j<n):
        if arr1[i]<=arr2[j]:
            print(arr1[i],end=" ")
            i+=1
        else:
          print(arr2[j],end=" ")
          j+=1
    while(i<m):
            print(arr1[i],end=" ")
            i+=1
    while(j<n):
            print(arr2[j],end=" ")
            j+=1
    print("\n")

arr1=[1,2,3,4,5,6]
arr2=[4,5,6,7,8,9]
MergeArrays(arr1,arr2)

'''
Time complexity: O(m+n)
Space Complexity: O(1)
'''

