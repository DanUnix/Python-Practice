# Author: Daniel Pulley
# Practicing Alogorithms
import random

#!/usr/bin/python

# merge Function
# Function takes given list arr and splits it into two temporary sublist
# Elements of both lists are compared one to another and put back into arr[l..m]
# Parameteres:  arr = given array
#               l = left index of list
#               m = middle index of list
#               r = right index of list
def merge(arr, l, m, r):
    n1 = m - l + 1      # get number of elements to the left of middle index -> arr[l..m]
    n2 = r -m           # get number of elements to the right of middle index -> arr[mid+1..r]

    # Create two temporary list of size n1 and n2 respectively
    left = [0] * (n1)
    right = [0] * (n2)

    # Copy elements from left to middle index of given arr to temporary list i-> left[0..n1] = arr[l..m] 
    for i in range(0, n1):
        left[i] = arr[l + i]
    # Copy elements from middle to right index of given arr to temporary list i-> right[0..n2] = arr[m+1..r] 
    for j in range(0, n2):
        right[j] = arr[m + j + 1]

    i = 0   # initial index of left sublist which is left half of arr - > [l..m]
    j = 0   # initial index of right sublist which is right half of arr -> [m+1..r]
    k = l   # initial index of merged list arr[l..r]

    # Compare elements from both left and right temporary list
    # and store them into arr[k]
    while i < n1 and j < n2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # Copy remaining elements from left[n1] temporary list if there are any
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    # Copy remaining elements from right[n2] temporary list if there are any
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


# merge_sort Function
# Function takes recursive approach using Divide and conquer method to
# split problem into sub problems to sort a given list of integers
# Parameters:   arr = given array
#               l = left index of list
#               r = right index  of list
def merge_sort(arr, l, r):
    # if l < r then perform merge_sort operation
    if l < r:
        mid = (l+r) / 2             # Get middle index of given list arr
        merge_sort(arr, l, mid)     # Run mergesort on left half of arr
        merge_sort(arr, mid+1, r)   # Run mergesort on right half of arr
        merge(arr, l, mid, r)       # merge subarrays in sorted order

# UTILITY FUNCTION
def display(arr):
    for i in range(0, len(arr)):
        print arr[i],
    else:
        print

# Generate a random list of 100 integers
# Able to get numbers between 1 and 1000
def generate_list():
    arr = [0] * 100
    for i in range(100):
        arr[i] = random.randint(1, 1000)
    return arr

def main():
    arr = [10, 2, 5, 8, 3, 4, 6]

    r_arr = generate_list()
    # Display unsorted List
    print("Displaying Unsorted List!\n")
    display(r_arr)

    # Run merge_sort and display sorted list
    print("\nDisplaying Sorted List!\n")

    merge_sort(r_arr,0, len(r_arr)-1)

    display(r_arr)

if __name__ == "__main__":
    main()
