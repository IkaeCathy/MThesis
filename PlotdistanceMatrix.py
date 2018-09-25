import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
#fname = "C:/DATA/Matrix_T_V5.txt"
#fname = "C:/DATA/Matrix111111.txt"
#fname = "C:/DATA/Matrixoabcdefgh.txt"
fname ="C:/Users/user1/Desktop/Unibe/Research/05092017/Meeting29.09.2017/Forms/NewDatafiles/Selectedimages/Matrices/Matrix_T_V777.txt"
myArray = []
textFile = open(fname)
lines = textFile.readlines()
#print(lines[0], lines[1], lines[2])
for line in lines[3:]:
    #print(line)
    lines=line.rstrip('\n')
    lines = lines.replace("[", "")
    lines =lines.replace("]", "")
    lines=lines.split(',')
    myArray.append(lines)

array = (myArray)  
#print([[float(i) for i in lst] for lst in array])
array1=[[float(i) for i in lst] for lst in array]
array1 = np.array(array1)
##df_cm1 = pd.DataFrame(array1, index = [j for j in i], columns = [j for j in i])
##plt.figure(figsize = (40,35))
##sn.heatmap(df_cm1, annot=None, linewidths=.9,cmap='RdBu')
##plt.show()
#plt.figure(1)
#ticks=np.linspace(0, 99,num=100)
ticks=np.linspace(0, (len(lines)-1),num=len(lines))
plt.figure(figsize = (200,200))
plt.imshow(array1, interpolation='none', cmap='RdBu')
cbar=plt.colorbar()
cbar.set_label('Distances', rotation=270, fontsize=20)
plt.xticks(ticks,fontsize=6)
plt.yticks(ticks,fontsize=6)
#plt.yticks.labelpad = 15
plt.grid(True)
plt.title('HED Matrix - RVL-CDIP-Specification', fontsize=26)
plt.xlabel('Document Classes', fontsize=26)
plt.ylabel('Document Classes', fontsize=26)
#mng = plt.get_current_fig_manager()
#mng.window.state('zoomed')
#plt.tight_layout()
plt.show()
