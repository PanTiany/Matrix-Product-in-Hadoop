#!/usr/bin/env python3
import sys
last_key = ()    
last_j = ' '
def product(A,B):
    result = 0
    for j in range(0,10000):
        result = result + int(A[j])*int(B[j])
        
    return(result)


for line in sys.stdin:
    key, value = line.split('\t')
    value = value.strip()
    value = value.replace('[','')
    value = value.replace(']','')
    value = value.replace("'",'')
    value = value.replace(",",'')
    value = value.replace("\n", '')
    value = value.split(' ')
    if(key != last_key):
        try:
            res = product(hash_A, hash_B)
            print('%s\t%s' %(key,str(res)))
        except:
            pass
        hash_A = [0 for zero in range(10000)]
        hash_B = hash_A 
        last_key = key
    j = int(value[1])-1
    if(value[0] == 'A'):
        hash_A[j] = value[2]
        #print('Append A')
    elif(value[0] == 'B'):
        hash_B[j] = value[2]
    else:
        pass    
