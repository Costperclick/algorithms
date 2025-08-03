"""
Merge sort: 

This algorithms is decent (O (n log(n) yet it eats a lot of memory by dividing the original list in 
multiples smaller copies. Also, it's pretty slow when dealing with small lists.)
Guess we can also call it "recursive divide and conquer" (split the list in a multiple of >= len(array) = 1) before merging one by one. 

Complexity : 
O(n log(n))

=== Pseudo code === 

Divide : 
The algorithm consists of two separate functions, merge_sort() and merge().
merge_sort() divides the input array into two halves, calls itself on each half,
and then merges the two sorted halves back together in order.
The merge() function merges two already sorted lists back into a single sorted list. At the lowest level of recursion,
the two "sorted" lists will each only have one element.
Those single element lists will be merged into a sorted list of length two, and we can build from there.
In other words, all the "real" sorting happens in the merge() function.

merge_sort() pseudocode:
Input: A, an unsorted list of integers
If the length of A is less than 2, it's already sorted so return it
Split the input array into two halves down the middle
Call merge_sort() twice, once on each half
Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls

merge() pseudocode:
Inputs: A and B. Two sorted lists of integers
Create a new final list of integers.
Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
Use a loop to compare the current elements of A and B. If an element in A is less than or equal to its respective element in B,
add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j.
Continue until all items from one of the lists have been added.
After comparing all the items, there may be some items left over in either A or B. Add those extra items to the final list.
Return the final list.

"""
import random
import time

# Merge sort algorithm : 

#Divide recursively and call conquer
def merge_sort(shuffled_list:list):
    if not isinstance(shuffled_list, list):
        raise TypeError('Argument must be a list')
    
    # Recursion ends here
    if len(shuffled_list) <= 1:
        return shuffled_list
    
    l = shuffled_list
    mid = len(l) // 2
    f_half = l[0:mid]
    s_half = l[mid::]
       
    # Recursion starts here 
    left_sorted = merge_sort(f_half)
    right_sorted = merge_sort(s_half)
    merged_list = merge(left_sorted, right_sorted)
    return merged_list
    
# Conquer :
def merge(left_sorted, right_sorted):
    
    i = 0
    j = 0
    final_list = []
    
    # Majority of element are sorted here
    while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] <= right_sorted[j]:
                final_list.append(left_sorted[i])
                i += 1
            else:
                final_list.append(right_sorted[j])
                j += 1
    
    # Leftovers are handled here : 
    while i < len(left_sorted):
        final_list.append(left_sorted[i])
        i += 1

    while j < len(right_sorted):
        final_list.append(right_sorted[j])
        j += 1
        
    return final_list
            


    