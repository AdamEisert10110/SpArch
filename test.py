import random
import numpy as np
import pandas as pd
import math
from scipy.sparse import csr_matrix
import pdb
import queue

random.seed(0)


count = 0
buffer_size = 12

#look_ahead_fifo = queue.Queue()
look_ahead_fifo = []
replacement_buffer = [None] * 12

#look_ahead_fifo.put(), .get()

#overall, need array merger program


#Will have state machine to run this, each step, call state machine to increment pointer
#Count is just number of steps
def state_machine():
    global count
    count += 1


def load_matrices():

    matrix_a = np.column_stack(([1,0,0,0,0],
                                [0,2,3,0,0],
                                [0,0,0,8,2],
                                [6,0,0,0,5],
                                [1,0,0,0,0]))

    matrix_b = np.column_stack(([0,0,4,0,0],
                                [0,1,0,8,0],
                                [0,0,3,0,2],
                                [0,9,0,0,0],
                                [0,0,0,0,6]))
                                

    return matrix_a, matrix_b

def to_csr(matrix):

    v = []
    col_index = []
    row_index = [0]

    current_col = 0
    current_row = 0

    max_col = np.shape(matrix)[0]
    max_row = np.shape(matrix)[1]


    val_count = 0

    
    #pdb.set_trace()
    
    for i, i_value in enumerate(matrix):

        val_count = 0
        
        for ii, ii_value in enumerate(i_value):
            
            if(ii_value != 0):
                v.append(ii_value)
                val_count += 1

                col_index.append(ii)
            if(ii == max_col - 1):
                row_index.append(val_count + row_index[len(row_index)-1])

    return([v, col_index, row_index])
                
            


#Comparator array merger



#Parallel Merge Unit

#Hierarchical Parallel Merge Unit

#Merge Tree

#Adders and Zero eliminator

#Matrix Condensing

#Huffman Tree scheduler


#place a columns in Look_ahead_fifo
def a_col_fetcher(csr_a):

    col_a = csr_a[1]

    for i, value in enumerate(col_a):
        look_ahead_fifo.append(value)
        
        

def distance_list_builder(csr_b):

    
    while(len(look_ahead_fifo) != 0):

        row_number = look_ahead_fifo.pop(0)

        current_rows = []

        distance_arr = []
        for i in look_ahead_fifo:
            if i not in distance_arr:
                distance_arr.append(i)

                

        rows_needed = csr_b[2][row_number+1] - csr_b[2][row_number]
        rows_start = csr_b[2][row_number]
        rows_end = csr_b[2][row_number+1]
            

        #this is an array of the actual values
        row_values = csr_b[0][rows_start:rows_end]

        a = []
        #an array of row "values"
        for i in range(rows_end - rows_start):
            a.append[i]

        
        full_values = [str(row_number) + ':' + str(x) for x in row_values]

        for i in replacement_buffer:
            val = i.split(':')[0]
            current_rows.append(val)

            

        #check if values are in buffer
        if not all(x in full_values for x in replacement_buffer):

            i = 0
            
            
    
        prefetcher(row_number, csr_b, distance_arr)
        
    

#Row Prefetcher

#col1 of a needs Row1 of b

def prefetcher(row_number, csr_b, distance_arr):
    i = 0

    #all(x in a for x in b)

    

    

#csr[0] is the value
#csr[1] is the column
#csr[2] is the row
if __name__ == "__main__":

    matrix_a, matrix_b = load_matrices()

    csr_a = to_csr(matrix_a)
    csr_b = to_csr(matrix_b)

    a_col_fetcher(csr_a)

    #might be able to be run threaded with a_col_fetcher
    #distance_list_builder(csr_b)

    

