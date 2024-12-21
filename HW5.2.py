import numpy as np


#2.1
def checkerboard():
    
    return np.zeros((8, 8), dtype=int)

#2.2
def checkerboard():
   
    board = np.zeros((8, 8), dtype=int)
    
    for i in range(0, 8, 2): 
        board[i, 0::2] = 1  
    return board

#2.3
def checkerboard():
   
    board = np.zeros((8, 8), dtype=int)
   
    for i in range(0, 8, 2):  
        board[i, 0::2] = 1
    
    for i in range(1, 8, 2):  
        board[i, 1::2] = 1  
    return board

#2.4
def reverse_checkerboard():
    
    board = np.zeros((8, 8), dtype=int)
    
    for i in range(0, 8, 2):  
        board[i, 1::2] = 1  
    
    for i in range(1, 8, 2):  
        board[i, 0::2] = 1  
    return board

