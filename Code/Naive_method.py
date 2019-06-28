#!/usr/bin/env python3

import sys
import numpy as np
import time
import multiprocessing 
from functools import partial 


start_time = time.time()
num = 10000
A = np.zeros((num,num))
B = np.zeros((num,num))

for line in sys.stdin:
    line = line.split('\t')
    #print(int(line[3])) 
    i = int(line[1])
    j = int(line[2])
    value = line[3].replace('\n','')
    #print(int(value))
    if(line[0] == 'A'):
        A[i-1, j-1] = int(value)
    if(line[0] == 'B'):
        B[i-1,j-1] = int(value)


def calculate_line(num, A,B,i):
    C_line = np.zeros((1,num))
    for j in range(0,num):
        for k in range(0,num):
            C_line[0,j] = C_line[0,j] + A[i,k]*B[k,j]
   # print(i)
    return(C_line)


NUM_WORKERS = 16
pool = multiprocessing.Pool(processes=NUM_WORKERS)
func = partial(calculate_line, num, A,B)
C = pool.map(func, list(range(0,num)))
pool.close()
pool.join()

end_time = time.time()
#print(A)
#print(B)
#print(C)
print("Time for product is %s secs"%(end_time - start_time))
