# Time Complexity : θ(n log(n))  
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : No
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  i = ( l - 1 )
  x = arr[h]
 
  for j in range(l, h):
      if   arr[j] <= x:

          # increment index of smaller element
          i = i + 1
          arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return (i + 1)


def quickSortIterative(arr, l, h):

  # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
 
    # initialize top of stack
    top = -1
 
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array

        p = partition( arr, l, h )
 
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

def printList(arr): 
    for i in range(len(arr)):
      print(arr[i])

if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7] 
    n = len(arr) 
    print ("Given array is")  
    printList(arr) 
    quickSortIterative(arr,0,n-1) 
    print("Sorted array is: ") 
    printList(arr)
    
