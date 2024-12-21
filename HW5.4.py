import numpy as np

def secondLargest(arr):
    
    sorted_arr = np.sort(arr, axis=0)[::-1]
   
    return sorted_arr[1]