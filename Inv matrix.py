import typing_extensions
import numpy as np
#实现键入整个矩阵的过程
h=int(input("Please input the number of matrix rows"))
l=int(input("Please input the number of matrix lists"))
lst=[]
for i in range(1,h+1):
    print("Plesase input"+str(i)+"row of the matrix.")
    lst.extend(input().split())
A=np.array(lst)
A.shape=(h,l)
A = A.astype(int)
A=np.matrix(A)
print(A.I)
print(type(A))