#!/usr/bin/python3

import numpy as np

dimensions=input("Enter the size of array (like: 3X4 or 6X8)::")
size=dimensions.split("X")
array=np.random.randint(5,size=(int(size[0]),int(size[1])))
f=open("data.txt","w")
f.write(str(array))
f.close

