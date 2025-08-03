"""
Quick sort:

Probably the most famous “divide and conquer” algorithm.
It has a very good average time complexity of O(n log n), works in-place (so it doesn’t need a lot of extra memory),
and is usually faster than merge sort in practice. downside? worst-case complexity can degrade to O(n²),
especially if the pivot choice is unlucky (ex: always picking the smallest / largest element in an already sorted array),
hence the classical trick of randomizing the pivot.

Complexity:
Best / Average:  O(n log n)
Worst case:      O(n²)

=== Pseudo code ===

The idea is:
Choose a pivot.
Partition the list into 2 parts: elements smaller than pivot go on one side, elements bigger go on the other.
Recursively quick_sort the left part and the right part.
Concatenate ( sorted_left + pivot + sorted_right ) and return.

quick_sort() pseudocode:
Input: A, an unsorted list
If len(A) <= 1, return A (already sorted)
Pick a pivot element (often middle or random)
Partition the remaining elements into two sublists:
    - left:    elements < pivot
    - right:   elements >= pivot
Call quick_sort(left) and quick_sort(right)
Return quick_sort(left) + [pivot] + quick_sort(right)

Notes on performance:
- In-place versions typically use a “partition” function and index swapping instead of creating new lists.
- Randomized pivot = crucial trick to avoid worst-case behavior on pre-sorted or adversarial input.
"""


import random
import time


def create_list(list_lenght):
    new_list = []
    for i in range(0, list_lenght):
        new_list.append(i)
    random.shuffle(new_list)
    return new_list


def quick_sort(l, low, high):
    if low < high:
        middle = partition(l, low, high)
        quick_sort(l, low, middle - 1)
        quick_sort(l, middle + 1, high)

        
def partition(l, low, high):
    pivot = l[high]
    i = low - 1
    for j in range(low, high):
        if l[j] < pivot:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i + 1], l[high] = l[high], l[i + 1]
    return i + 1


# ===== TESTING ======
start = time.time()
foo = create_list(1000000)
foo_sorted = quick_sort(foo, 0, len(foo)-1)
print(foo)
end = time.time()
print("Sort took", {end - start}, "seconds")


