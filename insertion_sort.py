"""
I found that i was easier to understand as follow : 
i = current_index, this value will always grow, never gets indented. 
j = key_alue of current index, it's the value we want to sort
j-1 = sorted_index, it's the index of the value just before j, and we always compare sorted_index with key_value
"""

import time
import random


def generate_list():
    n_list = []
    for i in range(0,10000):
        n_list.append(i)
    random.shuffle(n_list)
    return n_list

def insertion_sort(nums):
    for current_index in range(1, len(nums)):
        key_value = nums[current_index]
        sorted_index = current_index - 1
    
        while sorted_index >= 0 and nums[sorted_index] > key_value:
            nums[sorted_index + 1] = nums[sorted_index]
            sorted_index -= 1
        
        nums[sorted_index +1] = key_value
        
    return nums
 

a = generate_list()
a = insertion_sort(a)
print(a)


start = time.time()  
insertion_sort(a)  
end = time.time() 

print("Durée :", end - start, "secondes")