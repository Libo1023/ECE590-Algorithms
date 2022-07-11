"""
Math 560
Project 1
Fall 2021

Partner 1: Libo Zhang (NetID - lz200)
Partner 2:
Date: October 26, 2021
"""

"""
SelectionSort

This function takes a list (unsorted/sorted) as input,
and returns a sorted list as output.
"""
def SelectionSort(listToSort) :
    length = len(listToSort)

    # This outside for loop is to
    # increment the index k.
    for i in range(0, length - 1) :

        # Store the index separating the sorted
        # and unsorted components starting at
        # the front of the array, i.e., k = 0.
        k = i

        # Iteratively search the unsorted
        # component for the minimum element.
        for j in range(i + 1, length) :
            if listToSort[j] < listToSort[k] : 
                k = j
                
        # When the minimum of the unsorted array
        # is found, place it at the end of the
        # sorted component (at location k).
        place = listToSort[i]
        listToSort[i] = listToSort[k]
        listToSort[k] = place

    return listToSort

"""
InsertionSort

This function takes a list (unsorted/sorted) as input,
and returns a sorted list as output.
"""
def InsertionSort(listToSort) :
    length = len(listToSort)

    # This outside for loop is to 
    # increment the index k.
    for i in range(0, length) :

        # Store the index separating the sorted
        # and unsorted components starting at
        # the front of the array.
        k = i - 1
        to_sort = listToSort[i]
        while (listToSort[k] > to_sort) and (k >= 0) :

            # Iteratively insert the element 
            # into the sorted component.
            place = listToSort[k + 1]
            listToSort[k + 1] = listToSort[k]
            listToSort[k] = place

            # Search backwards
            k = k - 1

    return listToSort

"""
BubbleSort

This function takes a list (unsorted/sorted) as input, 
and returns a sorted list as output.
"""
def BubbleSort(listToSort) :
    length = len(listToSort)
    flag = 1 
    # Repeat until no more swaps are made.
    while (flag) :
        flag = 0
        # Iterate through the array.
        for i in range(1, length) :
            # Compare every two adjacent elements.
            if listToSort[i - 1] > listToSort[i] :
                # If they are out of order, swap them.
                place = listToSort[i]
                listToSort[i] = listToSort[i - 1]
                listToSort[i - 1] = place
                # Repeat until no more swaps are made.
                flag = 1
        # Repeat until no more swaps are made.
        length = length - 1
    
    return listToSort

"""
MergeSort

This function takes a list (unsorted/sorted) as input, 
and returns a sorted list as output.
"""
def MergeSort(listToSort) :
    length = len(listToSort)
    # Base Case - Array has 1 element, it is sorted.
    if length > 1 :
        # Split the array into two halves
        # Use floor division to always have an integer index.
        half_index = length // 2
        left_list = listToSort[:half_index]
        right_list = listToSort[half_index:]

        # Recursively sort each half.
        MergeSort(left_list)
        MergeSort(right_list)

        # Next, merge the already sorted halves.
        left = 0
        right = 0
        final = 0

        left_length = len(left_list)
        right_length = len(right_list)

        # Iterate through them simultaneously.
        while (left < left_length) and (right < right_length) :
            # Compare their smallest elements.
            # The smaller of the two gets removed and
            # inserted into the merged array.
            if left_list[left] < right_list[right] :
                listToSort[final] = left_list[left]
                left = left + 1
            else :
                listToSort[final] = right_list[right]
                right = right + 1
            final = final + 1

        # Make sure no element in the left half
        # is left behind.
        while left < left_length :
            listToSort[final] = left_list[left]
            left = left + 1
            final = final + 1
        # Make sure no element in the right half
        # is left behind.
        while right < right_length :
            listToSort[final] = right_list[right]
            right = right + 1
            final = final + 1
    
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.

This function takes a list (unsorted/sorted) as input,
and returns a sorted list as output.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None :
        j = len(listToSort)
    if j <= 1 :
        return

    left_recursive = i  
    right_recursive = i + j - 1
    front = left_recursive
    back = right_recursive

    # It is always best to split the array in half because
    # this minimizes the size of the largest recursive call.
    # Use floor division to always have an integer index.
    pivot_index = (front + back) // 2
    pivot = listToSort[pivot_index]

    # Partition the array based on the pivot.
    # Put everything smaller than the pivot in front and
    # put everything larger than the pivot in back.
    while front <= back :
        while (front <= back) and (listToSort[front] < pivot) :
            front = front + 1
        while (front <= back) and (listToSort[back] > pivot) :
            back = back - 1
        if front <= back :
            place = listToSort[front]
            listToSort[front] = listToSort[back]
            listToSort[back] = place
            front = front + 1
            back = back - 1

    # Recurse on each partition.
    QuickSort(listToSort, left_recursive, back - left_recursive + 1)
    QuickSort(listToSort, front, right_recursive - front + 1)



"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
