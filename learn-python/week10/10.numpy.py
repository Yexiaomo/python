#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
## numpy库 可用来存储和处理大型矩阵
### numpy的组成与功能
#### numpy(Numeric Python)可以理解为一个python实现的科学计算包。包括:
- 强大的N维数组对象Array；
- 成熟的函数库
- 实用的线性代数、傅里叶变换和随机数生成函数
- 提供了许多高级的数值编程工具，如：矩阵数据类、矢量处理，以及精密的运算库
#### numpy 的主要对象是同种元素的多维数组
- 维度（dimension） 叫做轴（axes）
- 轴的个数叫做秩（rank）
- e.g. 在3D空间一个点的坐标[1,2,3]是一个秩为 1 的数组.因为它只有一个轴.轴长为3
- e.g. 在[[1, 0, 0], [0, 1, 2]]这个例子中,数组的秩为2(它有两个维度).第一个维度长度为2,第二个维度长度为3
#### numpy的数组类被称为ndarray, 通常被称作数组.
- 注意numpy.array 和标准python库类array.array并不相同,后者只处理一维数组和提供少量功能.
- ndarray对象属性主要见下表: 例如其中 .shape 表示数组的维度, .size 表示数组元素的总个数

|属性         |解释             |
|-            |-               |
|ndarray.shape|数组的维度,这是一个指示数组在每个维度上大小的整数元组|
|ndarray.size |数组元素的总个数,等于shape属性中元组元素的乘积|
|ndarray.dtype|一个用来描述数组中元素类型的对象, 可以通过使用标准python类型创造dtype
|ndarray.itemsize|数组中每个元素字节的大小|
|ndarray.data|包含实际数组元素的缓冲区,通常我们通过索引引用数组元素,不使用这个属性|

e.g.
'''
'''python
>>>from numpy import *
>>>a = arange(15).reshape(3,5)
>>> a = arange(15).reshape(3,5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.ndim
2
>>> a.dtype.name
'int32'
>>> a.itemsize
4
>>> a.size
15
>>> type(a)
<class 'numpy.ndarray'>
>>> b = array([6,7,8])
>>> b
array([6, 7, 8])
>>> type(b)
<class 'numpy.ndarray'>
>>>
'''
'''
- 创建数组方法1
可以使用array函数利用常规的python列表和元组创造数组
所创建的数组类型由原序列中的元素类型决定
e.g.
'''
'''python
>>> from numpy import *
>>> a = array([2,3,4])
>>> a
array([2, 3, 4])
>>> a.dtype
dtype('int32')
>>> b = array([1.2, 3.4, 5.1])
>>> a
array([2, 3, 4])
>>> b
array([ 1.2,  3.4,  5.1])
>>> b.dtype
dtype('float64')
>>>#一个常见的错误包括用多个数值参数调用 'array' 而不是提供一个由数值组成的列表作为一个参数
>>> a = array(1, 2, 3, 4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: only 2 non-keyword arguments accepted
>>> a = array([1,2,3,4]) #RIGHT
>>> c = array([[1,2],[3,4]], dtype=complex)
>>> c
array([[ 1.+0.j,  2.+0.j],
       [ 3.+0.j,  4.+0.j]])
>>>
'''
'''
- 创建数组方法2
numpy提供了一些使用占位符创建数组的函数
例如: 函数zeros创建一个全是0的数组;
      函数ones创建一个全1的数组;
      函数empty创建一个内容随机并且依赖与内存状态的数组。
默认创建的数组类型(dtype)都是float64
e.g.
'''
'''python
>>> zeros((3,4))
array([[ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]])
>>> ones((2,3,4), dtype=int16)
array([[[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]],

       [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]], dtype=int16)
>>> empty((2,3))
array([[  9.08835827e-315,   9.08836712e-315,   9.10694272e-315],
       [  1.09913990e-311,   1.09913990e-311,   1.09913990e-311]])
>>>
'''
'''
- 创建数组方法3
numpy提供一个arange的函数返回数组
e.g.
'''
'''python
>>> from numpy import *
>>> arange(10,30,5)
array([10, 15, 20, 25])
>>> arange(0, 2, 0.3)
array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])
>>>
'''
'''
- 打印数组
numpy以类似嵌套列表的形式显示
一维数组被打印成行; 二维数组成矩阵; 三维数组成矩阵列表。
e.g.
'''
'''python
>>> a = arange(6)
>>> a
array([0, 1, 2, 3, 4, 5])
>>> print(a)
[0 1 2 3 4 5]
>>> b = arange(12).reshape(4,3)
>>> print(b)
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
>>> c = arange(24).reshape(2,3,4)
>>> print(c)
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
>>>
'''
'''
#### numpy 基本运算
- 数组的算术运算是按元素进行->numpy中的乘法运算符*指示按元素计算
矩阵乘法可以使用dot函数或创建矩阵对象实现
e.g.
'''
'''python
>>> from numpy import *
>>> a = array([20, 30, 40, 50])
>>> b = arange(4)
>>> b
array([0, 1, 2, 3])
>>> a
array([20, 30, 40, 50])
>>> c = a - b
>>> c
array([20, 29, 38, 47])
>>> b ** 2
array([0, 1, 4, 9], dtype=int32)
>>> 10 * sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
>>> a < 35
array([ True,  True, False, False], dtype=bool)
'''
'''
- 非数组运算可以利用 ndarray 类方法实现
- 通用函数(ufunc) --numpy提供常见的数学函数(如 sin, cos, exp)
在numpy里这些函数作用按数组的元素运算,产生一个数组作为输出
e.g.
'''
'''python
>>> from numpy import *
>>> a = random.random((2,3))
>>> a
array([[  1.53506215e-01,   6.11371571e-03,   1.12949639e-01],
       [  3.06270776e-04,   1.02815374e-01,   5.85464689e-01]])
>>> a.sum()
0.96115590330548029
>>> a.min
<built-in method min of numpy.ndarray object at 0x00000205F7C4AD00>
>>> a.min()
0.00030627077619060916
>>> a.max()
0.58546468851120936
>>> b =arange(12).reshape(3,4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> b.sum(axis = 0)
array([12, 15, 18, 21])
>>> #sum of each column
...
>>> b.min(axis = 1)# min of each row
array([0, 4, 8])
>>> b.cumsum(axis = 1)# cumnlative sum along each row
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]], dtype=int32)
>>>
'''
'''
- 数组还可以被索引、切片和迭代
e.g.
'''
'''python
>>> a = arange(10) ** 3
>>> a
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729], dtype=int32)
>>> a[2]
8
>>> a[2:5]
array([ 8, 27, 64], dtype=int32)
>>> a[:6:2]
array([ 0,  8, 64], dtype=int32)
>>> a[:6:2] = -1000
>>> a
array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729], dtype=int32)
>>> a[::-1] # reverse a
array([  729,   512,   343,   216,   125, -1000,    27, -1000,     1, -1000], dtype=int32)
>>> for i in a:
...     print(i ** (1/3.),)
...
nan
1.0
nan
3.0
nan
5.0
6.0
7.0
8.0
9.0
>>>
'''
'''
#### 矩阵运算
- numpy对于多维数组的运算,缺省情况下并不使用矩阵运算,对数组进行矩阵运算,可调用相应的函数.
- numpy库也提供了matrix类,使用matrix类创建的是矩阵对象,
它们的加减乘除运算缺省采用矩阵方式计算,用法和matlba 十分类似
e.g.
'''
'''python
>>> from numpy import *
>>> m = matrix([[1, 2, 3], [5, 5, 6], [7, 9 ,9]])
>>> m * m ** -1
matrix([[  1.00000000e+00,   0.00000000e+00,   0.00000000e+00],
        [  4.44089210e-16,   1.00000000e+00,   4.44089210e-16],
        [  0.00000000e+00,  -4.44089210e-16,   1.00000000e+00]])
>>>
'''
'''
- 矩阵中更高级的一些运算可以在 numpy 的线性代数子库 linag 中找到.
例如inv函数计算逆矩阵,solve函数可以求解多元一次方程组。

#### 函数和方法的总览
下面是一个分类排列目录总揽，可通过手册即用即学
|分类                     |函数                             |
|--                       |--                               |
|创建数组|arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like|
|转化    |astype, atleast 1d, atleast 2d, atleast 3d, mat    |
|操作    |array split, column stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, item, newaxis, ravel, repeat,reshap, resize, squeeze, swapaxes, take, transpose, vsplit,vstack|

'''

## GPS定位计算的程序基本实现
'''
### GPS定位的基本原理
- 基本原理
是根据高速运动卫星的瞬间位置作为已知的起算数据,采用空间距离-后方交会的方法 确定待测点的位置.
假设t时刻在地面待测点上安置GPS接收机，可以测定GPS信号到达接收机的时间△t，
再加上接收机所接收到的卫星星历等其它数据 就可以确定一个方程组进行求解。
- e.g.
假设地球上一个点R，同时收到6颗卫星（S1,S2,…,S6）发射的信号，假设接受信息如下表所示:
其中x，y表示卫星的经纬度，z表示 的高度。
由于上述6个卫星和地球在高速运动，从卫星发出的位置信息以光速传输到GPS接收端需要一定的时间
假设(x,y,z,t)表示R当前的位置，t是R的相对时间，
卫星S1（发出信号时刻）到（当前接收时刻)满足以下关系(其中c是光速)
该公式表示以(x, y, z,t)为参数的(欧式空间距离)与信号传输距离相等
  (x-3)^2 + (y-2)^2 + (z-3)^2 = [(10010.00692286– t)*c]^2
对于卫星S1,S2,…,S6，满足方程组

(x-3)^2 + (y-2)^2 + (z-3)^2 - [(10010.00692286 – t)*c]^2 = 0
(x-1)^2 + (y-3)^2 + (z-1)^2 - [(10013.34256381 - t)*c]^2 = 0
(x-5)^2 + (y-7)^2 + (z-4)^2 - [(10016.67820476 – t)*c]^2 = 0
(x-1)^2 + (y-7)^2 + (z-3)^2 - [(10020.01384571 – t)*c]^2 = 0
(x-7)^2 + (y-6)^2 + (z-7)^2 - [(10023.34948666 – t)*c]^2 = 0
(x-1)^2 + (y-4)^2 + (z-9)^2 - [(10030.02076857 – t)*c]^2 = 0

其中，光速为常数c=0.299792458km/us，上述方程组是非线性的
但很容易将所有二次项都消去（每个公式减去第一个公式)，从而得到：

  |  4  -4 -12 3.59751 |                 |  35971.1  |
 |                      |  | x |        |             |
 |   0  -2 -16 2.99792  |               |   29957.2   |
 |                      |  | y |        |             |
 |   8   6 -10 2.39843  |          =    |   24031.4   |
 |                      |  | z |        |             |
 |   0   6 -12 1.79875  |               |   17993.5   |
 |                      |  | t |        |             | 
  | 12  4  -4 1.19917  |                 |  12059.7  |

此时，上述等式变成了A*X=B形式，根据线性代数方法 X=A-1*B
即只需对系数矩阵求逆，再乘以常数矩阵便可以得到方程组的解。

'''
# 用到的函数 numpy.linalg.inv(a) 计算矩阵a的逆矩阵
# 用到的函数 numpy.dot(a,b) 计算矩阵a与矩阵b的点积
'''
参考数据
3 2 3 10010.00692286
1 3 1 10013.34256381
5 7 4 10016.67820476
1 7 3 10020.01384571
7 6 7 10023.34948666
1 4 9 10030.02076857

结果应为:
[[ 5.00000000e+00]
 [ 3.00000000e+00]
 [ 1.00000000e+00]
 [ 1.00000000e+04]]

'''

from numpy import *
i = 1
c = 0.299792458  #光速
x = zeros((6,4)) #存储6颗卫星的(x,y,z,t)参数
while i<= 6:
    print("%s %d" % ("please input (x,y,z,t) of group", i))
    temp = input()
    x[i-1] = temp.split()
    j = 0
    while j<4:
        x[i-1][j] = float(x[i-1][j])
        j = j+1
    i = i+1

a = zeros((4,4)) #系数矩阵
b = zeros((4,1)) #常数项
j = 0
while j<4:
    a[j][0] = 2* (x[5][0] - x[j][0])
    a[j][1] = 2* (x[5][1] - x[j][1])
    a[j][2] = 2* (x[5][2] - x[j][2])
    a[j][3] = 2* c*c *(x[j][3] - x[5][3])
    b[j][0] = x[5][0] * x[5][0] - x[j][0] * x[j][0] + \
              x[5][1] * x[5][1] - x[j][1] * x[j][1] + \
              x[5][2] * x[5][2] - x[j][2] * x[j][2] + \
              c*c * (x[j][3] * x[j][3] - x[5][3] * x[5][3])
    j = j+1

a = linalg.inv(a) #系数矩阵求逆
print(dot(a,b))