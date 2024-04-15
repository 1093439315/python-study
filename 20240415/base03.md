# Python 基础第三课

## 序列之 字符串 类

### 1. 字符串的内置方法 Built-In Functions of The String:

- 通用类（与列表、元组共用）
- 转换类
- 判断类
- 替换类

#### 通用类

|方法|说明|
|:---:|:---|
| .index(el) | 取得元素 el 的下标（索引）|
| .rindex(el)|从右向左、取得元素 el 的下标（索引）|
| .count(el)|统计元素 el 计数 |
|切片|sequence[start-index : end-index : dir-step]<br>start-index默认值=0, end-index默认值=长度<br>dir-step默认值=1|


#### 转换类

|方法|说明|
|:---:|:---|
|.upper()|转为大写|
|.lower()|转为小写|
|.title()|词首大写|
|.capitalize()|句首大写|
|.swapcase()|大转小，小转大|
|.split()<br>.split(el)| 拆分字符串，默认拆分字符是空白`\t\n\r\v `<br>el: 指定拆分字符|


#### 判断类

|方法|说明|
|:---:|:---|
|.isalpha()|判断是否全字母 A-Z a-z|
|.isdigit()|判断是否全数字 0-9|
|.isnumeric()|判断全数字，包含中文数字（大小写），罗马数字|
|.isdecimal()|判断是否为十进制数字|
|.isalnum()|判断是否字母和数字A-Za-z0-9|
|.istitle()|判断是否词首大写|
|.isspace()|判断是否空白字符 '  ', `'\n'`, `'\t'`, `'\r'`, `'\v'`|


#### 替换类

|方法|说明|
|:---:|:---|
|.replace(old_str, new_str[, count])|用 new_str 替换 old_str, 可选 count默认全部|
|.strip()<br>.strip(el)|删除首尾空白符, 默认是`\t,\n\r\v `<br>el: 指定字符|
|.lstrip()<br>.lstrip(el)|删除左边空白符, 默认是`\t,\n\r\v `<br>el: 指定字符|
|.rstrip()<br>.rstrip(el)|删除右边空白符, 默认是`\t,\n\r\v `<br>el: 指定字符|


#### 格式化输出类

|方法|说明|
|:---:|:---|
|.center(width, fillchar)|'Hello world'.center(30, ' # ')|


### 格式化字符串


#### 1. % 模板

**语法：**
`'%*模板' % (字面量或变量, ...)`

|模板语法|说明|
|:---:|:---|
|%d|输出整数 digit|
|%nd|输出n位的整数|
|%0nd|输出n位的整数，不足补零|
|%f|输出浮点数，默认是小数点后6位|
|%.nf|输出指定小数点后n位的浮点数|
|%s, %ns|输出字符串或指定宽度n的字符串|
|%x, %X|输出十六进制数字 0-9, A-F x小写X大写|
|%c|输出字符，变量字面量是数字，输出对应的字符|
|%e, %E|科学记数法 1.246e5|


```python
a = 100
b = 123.456
c = 'Hello world'

d = '%d' % (a) # 中间的 % 连接符
print(d)

```


#### 2. format

**语法：**

` '{}'.format(字面量或变量)`


|模板语法|说明|
|:---:|:---|
|:d|输出整数 digit|
|:nd|输出n位的整数|
|:0nd|输出n位的整数，不足补零|
|:,|千分位格式输出 x,xxx,xxx |
|:f|输出浮点数，默认是小数点后6位|
|:.nf|输出指定小数点后n位的浮点数|
|:b|输出二进制数字|
|:o|输出八进制数字|
|:x, %X|输出十六进制数字 0-9, A-F x小写X大写|
|:c|输出字符，变量字面量是数字，输出对应的字符|
|:e, :E|科学记数法 1.246e5|
|:s, %ns|输出字符串或指定宽度n的字符串|
|:`<ns`|字符串默认向左对齐|
|:`>ns`|字符串向右对齐|
|:`^ns`|字符串居中对齐|


```python
a = 100
b = 123.456
c = 'Hello world'

d = '{}'.format(a)
print(d)


```

#### 3. f-string

**语法：**

` f'{字面量或变量:格式}'`

**格式符号与 format 相同**

```python
a = 100
b = 123.456
c = 'Hello world'

print(f'{a:06d}')

print(f'{b:.2f}')

print(f'{c:^30}')

```


## 列表的内置方法

- 添加
  - .append(el)
  - .insert(index, el)
- 删除（弹出）
  - .pop()
  - .pop(index)
  - .remove(index)
  - del object[index]
***

2024-04-15

__EOF__
