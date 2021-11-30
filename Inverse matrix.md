11.30 尝试编写 通过键入矩阵行列来输出逆矩阵

```python
import numpy as np

h=int(input("Please input the number of matrix rows"))      #保存矩阵行数

l=int(input("Please input the number of matrix lists"))     #保存矩阵列数

lst=[]

for i in range(1,h+1):

​    print("Plesase input"+str(i)+"row of the matrix.")

​    lst.extend(input().split())                             #实现将键入值存在一个列表中

A=np.array(lst)                                             #将列表转换为numpy数组

A.shape=(h,l)                                               #重构形状

A = A.astype(int)                                           #将str数据转为int

A=np.matrix(A)                                              #数组转为矩阵

print(A.I)                                                  #输出逆矩阵
```

