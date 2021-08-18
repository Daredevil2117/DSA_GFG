'''
Given two sorted arrays print union elements in sorted order
'''
'''
Naive Approach: Create one more array of size arr1+arr2 and store all elements of both array and sort it.
print all elements of new array with condition i==0 or arr[i]!=arr[i-1]
Time Complexity: O((m+n)*log(m+n))  m=len(arr1) and n=len(arr2)
Space Complexity: O(m+n)
Note: Naive solution works for unsorted arrays as well
''' 

def Union(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    i=j=0
    while(i<m and j<n):
        if i>0 and arr1[i]==arr1[i-1]:
            i+=1
            continue
        if j>0 and arr2[j]==arr2[j-1]:
            j+=1
            continue
        if arr1[i]<arr2[j]:
            print(arr1[i],end=" ")
            i+=1
        elif arr1[i]>arr2[j]:
            print(arr2[j],end=" ")
            j+=1
        else:
            print(arr1[i],end=" ")
            i+=1
            j+=1
    while(i<m):
        print(arr1[i],end=" ")
        i+=1
    while(j<n):
        print(arr2[j],end=" ")
        j+=1

arr1=[1,2,3,4,4,5]
arr2=[3,4,4,4,5,6,7]
Union(arr1,arr2)

'''
Time Complexity: O(m+n)
Space Complexity:O(1)
'''
