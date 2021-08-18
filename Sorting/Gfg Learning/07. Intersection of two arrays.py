'''
Given two soted arrays print the elements which are common in both
'''
'''
# Naive Approch 

def Intersection(arr1,arr2):
    n=len(arr1);m=len(arr2)
    for i in range(n):
        if i>0 and (arr1[i]==arr1[i-1]):
            i+=1
            continue
        for j in range(m):
            if arr1[i]==arr2[j]:
                print(arr1[i],end=" ")
                break
                                
Time Complexity: O(m*n)
Space Complexity:O(1)
Note: Naive approach works even when arrays are not sorted as it checks for all elements every time             
'''
def Intersection(arr1,arr2):
    n=len(arr1);m=len(arr2)
    i=0;j=0
    while(i<n and j<m):
        if i>0 and arr1[i]==arr1[i-1]:
            i+=1
            continue
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
        else:
            print(arr1[i],end=" ")
            i+=1
            j+=1

arr1=[1,2,3,4,4,5]
arr2=[3,4,4,4,5,6,7]
Intersection(arr1,arr2)

'''
Time Complexity: O(m+n)
Space Complexity: O(1)
'''

