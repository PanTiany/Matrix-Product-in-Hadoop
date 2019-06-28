#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.split('\t')
    # print(line[0])
    if(line[0] == 'A'):
        for k in range(1,10001):
            key = str(line[1]).zfill(3)+'0'+str(k).zfill(3)
            value =[line[0],line[2],line[3].replace('\n','')]
            print(key,'\t', value)
    elif(line[0] == 'B'):
        for i in range(1,10001):
            key = str(i).zfill(3)+'0'+str(line[2]).zfill(3)
            value =[line[0],line[1],line[3].replace('\n','')]
            print(key,'\t',value)
