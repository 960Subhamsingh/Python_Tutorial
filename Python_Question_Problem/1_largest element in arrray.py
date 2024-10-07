# Find the Largest element in an array

"""
Example 1:
Input:
 arr[] = {2,5,1,3,0};
Output:
 5
Explanation:
 5 is the largest element in the array. 

Example2:
Input:
 arr[] = {8,10,5,7,9};
Output:
 10
Explanation:
 10 is the largest element in the array. 
"""

def Largest(arr, n):


    max = arr[0]
    for i in range(0, n):
        if (max < arr[i]):
            max = arr[i]
    return max

if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    n = 5
    max = Largest(arr1, n)
    print("The largest element in the array is:", max)


    arr2 = [8, 10, 5, 7, 9]
    n = 5
    max = Largest(arr2, n)
    print("The largest element in the array is:", max)



from typing import List
def sortArr(arr: List[int]) -> int:
    arr.sort()
    return arr[-1]
if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    arr2 = [8, 10, 5, 7, 9]
    print("The Largest element in the array is:", sortArr(arr1))
    print("The Largest element in the array is:", sortArr(arr2))