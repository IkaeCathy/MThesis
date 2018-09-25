#used to obtain accuracy and show matched images

import numpy as np
import matplotlib.pyplot as plt
from directory import *
w = list_files('C:/DATA/NIST2-small')#('C:/DATA/MARG-small')
xi= [wi for wi in w if not wi.endswith('.gxl')]
fname = "C:/DATA/Matrix_T_V5.txt"#"C:/DATA/Matrixoabcdefgh.txt".....Distance Matrix file
myArray = []
textFile = open(fname)
lines = textFile.readlines()
correct=0
for line in lines:
    lines=line.rstrip('\n')
    lines = lines.replace("[", "")
    lines =lines.replace("]", "")
    lines=lines.split(',')
    myArray.append(lines)
for j in range(len(xi)):
    n = [x for x in xi if x != xi[j]]
    N = [xx for xx in myArray[j] if xx != myArray[j][j]]
    #print('minN=', min(N), 'minarrayj=', min(myArray[j]))
    
    #print()
    
        
    b1=(xi[j]).encode('unicode_escape')
    print('b1=',b1)
    
    c1=((b1.decode("utf-8").split('\\\\'))[1])
    #print("c1=",c1)
    
    b2=(n[N.index(min(N))]).encode('unicode_escape')
    print("b2=",b2)
    
    c2=((b2.decode().split('\\\\'))[1])
    #print("c2", c2)
    
    print("c1=",c1, "c2=",c2)
    if c1==c2:
        correct = correct+1
acc=correct/(len(xi))
print("acc",acc)
