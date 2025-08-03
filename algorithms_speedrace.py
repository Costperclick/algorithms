"""
Use this module to compare the speed of each algorithm given a list (idealy, the same for eveyone)
Note that some algorithms might get a "lucky timer" as, for instance, if the list is randomly already pre-sorted after random.shuffle, 
Insertion_sort would perform better than average (in this scenario only)
Have fun
"""

import time
import random


from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort, merge
from quick_sort import quick_sort
from create_list import create_randomised_list


# Create a random list with the desired lenght
foo = create_randomised_list(100000)


# Let the race begins !
foo_bubble_start = time.time()
foo_bubble_sort = bubble_sort(foo)
foo_bubble_end = time.time()

foo_insertion_start = time.time()
foo_insertion_sort = insertion_sort(foo)
foo_insertion_end = time.time()

foo_merge_start = time.time()
foo_merge_sort = merge_sort(foo)
foo_merge_end = time.time()

foo_quick_start = time.time()
foo_quick_sort = quick_sort(foo, 0, len(foo) - 1)
foo_quick_end = time.time()


print(
    f"====== RESULTS =======\n"
    f"Bubble Sort time    : {foo_bubble_end - foo_bubble_start}\n"
    f"Insertion Sort time : {foo_insertion_end - foo_insertion_start}\n"
    f"Merge Sort time     : {foo_merge_end - foo_merge_start}\n"
    f"Quick Sort time     : {foo_quick_end - foo_quick_start}"
)



