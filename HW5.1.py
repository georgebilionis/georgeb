import numpy as np 

def onlyOdd(arr):
    
    is_odd = np.all(arr % 2 == 1, axis=1)
  
    return arr[is_odd]