# Python 基础第二课


## 数据类型

- 数字
  - 整数 int
  - 浮点数 float
- 布尔值 bool
- 字符串 str
- 列表 list
- 元组 tuple
- 字典 dict
- None

## 运算符

- 算术运算符 `+, -, *, /, //, **, %`
- 比较运算符 `>, >=, <, <=, ==, !=, not ==`
- 位操作运算符 `<<, >>`
- 逻辑运算符 `and, or, not`
- 二元操作符 `+=, -=, *=, /=, //=, **=, %=`

```python
a = 10
b = 5

a = a + b  # a 的自增量是 b
# a = 10 + 5

a += b  # a += 5
```


## 程序结构

- 顺序结构
- 分支结构 id-elif-else

```python
if 条件表达式1:
	pass # 占位符，无其它作用
elif 条件表达式2:
	pass
else: # 隐含 条件表达式3
	pass

```


- 循环结构 while for-in

```python
while 条件表达式:
    # 满足条件循环执行
	pass
    if 条件表达式1:
    	continue  # 回到循环开头（跳过之下所有语句）
    if 条件表达式2:
    	break     # 跳出所有循环
else:
	# 不满足条件时执行
	pass


for 迭代变量 in 序列:
	pass
	# 满足条件循环执行
    if 条件表达式1:
    	continue  # 回到循环开头（跳过之下所有语句）
    if 条件表达式2:
    	break     # 跳出所有循环
else:
	# 不满足条件时执行
	pass

```








***

2024-04-10

__EOF__

