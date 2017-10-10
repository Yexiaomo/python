## Pandas [官方文档](http://pandas.pydata.org/pandas-docs/stable/pandas.pdf)
安装
    sudo pip install pandas
    # 安装指定版本
    sudo pip install -v pandas==0.20.3

### pandas数据类型简单操作
如何改变Series和DataFrame对象
- 增加或重排:重新索引
.reindex()能够改变或重排Series和DataFrame索引
|参数|说明|
|-|-|
|index,columns|新的行列自定义索引|
|fill_value|重新索引中,用于填充缺失位置的值
|method|填充方法,ffill当前值向前填充,bfill向后填充|
|limit|最大填充量|
|copy|True,生成新对象. False时,新旧相等不复制|

- 删除指定索引对象
.drop() 能够删除Series和DataFrame指定或列索引,并生成新的对象

### pandas索引类型常用方法
|方法|说明|
|-|-|
|.append(idx)|连接另一个Index对象,产生新的Index对象|
|.diff(idx)|计算差集, 产生新的Index对象|
|.intersection(idx)|计算交集|
|.union(idx)|计算并集|
|.delete(loc)|删除loc位置处的元素|
|.insert(loc, e)|在loc位置处增加一个元素e|

### pandas库的数据排序
注意: NaN排序时,统一放到末尾
.sort_index(axis=0, ascending=True)在指定轴上根据索引进行排序, 默认升序
.sort_values(axis=0, ascending=True)在指定轴上根据数值进行排序, 默认升序
- Series.sort_values(axis=0, ascending=True)
- DataFrame.sort_values(by, axis=0, ascending=True) # by:axis轴上的某个索引或索引列表

### 基本统计分析函数(适用于Series和DataFrame类型)
|方法|说明|
|-|-|
|.sum()|计算数据的总和,按0轴计算,下同|
|.count()|非NaN值的数量|
|.mean() .median()|计算数据的算术平均值,算术中位数|
|.var() .std()|计算数据的方差,标准差|
|.min() max()|计算数据的的最小值,最大值|
|.argmin() .argmax()|(适用于Series)计算数据最大值,最小值所在位置的索引位置(自动索引)|
|.idxmin() .idxmax()|(适用于Series)计算数据最大值,最小值所在位置的索引(自定义索引|
|.describe()|针对0轴(各列)的统计汇总|

### 累计统计分析函数(适用于Series和DataFrame类型, 累计计算)
|方法|说明|
|-|-|
|.cumsum()|依次给出前 1、2、...、n个数的和|
|.cumprod()|依次给出前 1、2、...、n个数的积|
|.cummax()|依次给出前 1、2、...、n个数的最大值|
|.cummin()|依次给出前 1、2、...、n个数的最小值|

### 累计统计分析函数(适用于Series和DataFrame类型, 滚动计算-->窗口计算)
|方法|说明|
|-|-|
|.rolling(w).sum()|依次计算相邻w个元素的和|
|.rolling(w).mean()|依次计算相邻w个元素的算术平均值|
|.rolling(w).var()|依次计算相邻w个元素的方差|
|.rolling(w).std()|依次计算相邻w个元素的标准差|
|.rolling(w).min() .max|依次计算相邻w个元素的最小值和最大值|

###  相关分析函数(适用于Series和DataFrame类型)
|方法|说明|
|-|-|
|.cov()|计算协方差矩阵|
|.corr()|计算相关系数矩阵,Person、Spearman、Kendall等系数|

## Pandas库的 Series类型

Series类型由一组数据及与之相关的数据索引组成

|索引|数据|
|-|-|
|index_0|data_a|
|index_1|data_b|
|index_2|data_c|

### Series类型可以由如下类型创建
- python列表
- 标量值
- python字典
- ndarray
- 其他函数

### Series类型的基本操作
Series类型包括index和value两部分
Series类型的操作类似ndarray类型
Series类型的操作类似python字典类型


## Pandas库的 Dataframe类型
Dataframe类型:
- 由一组共用相同索引的一组列组成
- 是一个表格型的数据类型,每列值类型可以不同
- 既有行索引(index), 也有列索引(column)
- 常用于表达二维数据,但可以表达多维数据

### DataFrame 类型可以由如下类型创建
- 二维ndarray对象
- 由一维ndarray,列表,字典,元组,或Series构成的字典
- Series类型
- 其他DataFrame类型