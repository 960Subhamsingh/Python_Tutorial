# Check if an Array is Sorted

"""
Example 1:
Input:
 N = 5, array[] = {1,2,3,4,5}
Output
: True.
Explanation:
 The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

"""

"""
Example 2:
Input:
 N = 5, array[] = {5,4,6,7,8}
Output
: False.
Explanation:
 The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False.

Here element 5 is not smaller than or equal to its future elements.

"""

def isSorted(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False

    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    ans = isSorted(arr, n)
    if ans:
        print("True")
    else:
        print("False")