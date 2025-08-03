"""
This algorithm is so bad it becomes funny
Complexity : O(n^2).

===== Pseudo-code : ======

Bubble sort repeatedly steps through a slice and compares adjacent elements, 
swapping them if they are out of order. 
It continues to loop over the slice until the whole list is completely sorted. Here's the pseudocode:

1. Set swapping to True
2. Set end to the length of the input list
3. While swapping is True:
    3.1 Set swapping to False
    3.2 For i from the 2nd element to end:
    3.3 If the (i-1)th element of the input list is greater than the ith element:
        3.3.1 Swap the (i-1)th element and the ith element
        3.3.2 Set swapping to True
        3.3.3 Decrement end by one
Return the sorted list

"""

import time
import random


def generate_list(max):
    n_list = []
    for i in range(0,max):
        n_list.append(i)
    random.shuffle(n_list)
    return n_list

# code : 
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):  
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j] 
                swapped = True
        if not swapped:
            break  
    return nums


start = time.time()
l = generate_list(10000)
l = bubble_sort(l)
end = time.time()
print("Durée :", end - start, "secondes")