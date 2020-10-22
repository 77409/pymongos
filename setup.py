import codecs
import os
import sys
try:
    from setuptools import find_packages,setup
except:
    from distutils.core import find_packages,setup

def read(fname):
    return """
# pymongos
简化了一些`pymongo`的操作，像操作`json`一样操作你的数据。
因为日常用增删查改最多，所以简化主要是围绕这三个操作来的。

## 安装
### 先装依赖
```
python -m pip install pymongos
python3 -m pip install pymongos
```

## 连接数据库

### 无密码连接
```
from pymongos import mongodb
table = mongodb(host='127.0.0.1', db="test", table="test")

# 无日志
table = mongodb(host='127.0.0.1', db="test", table="test", level="debug")
```

### 密码连接
```
from pymongos import mongodb
table = mongodb(host='127.0.0.1', db="test", table="test", user="admin", passwd="123456789")
```

## 插入数据
### 不设置_id（MongoDB随机生成）

```
table += {"字段1": "数据1", "字段2": "数据1"}
```
or
```
table + {"字段1": "数据1", "字段2": "数据1"}
```
![](https://raw.githubusercontent.com/77409/e4ting/master/插入-随机ID.jpg)

> 因为分配的ID是随机的，不建议使用

### 设置_id
```
table["设置_id"] = {"字段1": "数据3", "字段2": "数据4"}
table["test"] = {"爱好": "看书", "书名": "鬼吹灯"}
```
![图片传不上来了](https://raw.githubusercontent.com/77409/e4ting/master/插入指定ID.jpg)

## 删除数据
仅支持指定key方式
```
del table["设置_id"]
```

## 修改
```
table["test"] = {"书名": "鬼吹灯和三体"}
table["test"] = {"书名": "《鬼吹灯》《三体》", "爱好": "看书&游泳"}
table["test"] = {"name" : "e4ting"}
```

## 取数据
### 表长度
```
len(table)
```

### _id是否存在
```
if "test" in table:
    print("yes")
```

### 获取所有_id
```
table.keys()
```


### 根据_id取
```
data = table["test"]
print(data)
```

### 取整个表数据
    数据少的时候才可以这么豪横的用
```
table[:]
# 或
table.get()
```

### 遍历表
    表太大的时候，迭代取
```
for _ in table:
    print(_)
```

### 过滤
```
table[::{"name":"e4ting"}]
# 或
table.get(name="e4ting")
# 或 字段名有中文时
table.get(**{"字段1":"数据1"})
```

### 分段
```
table[:10]
# 或
table[1:10]
# 或
table.get(limit=10, offset=1)
```

## 排序
```
# 按 _id 倒序
table[::-1]

# 按 _id 倒序，分段
table[0:10:-1]

# 按 name 正序
table[::"name"]

# 按 name 正序，分段
table[0:10:"name"]

# 按 name 倒序
table[::"!name"]

# 按 name 倒序，分段取
table[0:10:"!name"]
```

### 搜索
```
table.search(name="4ting")
```
### 搜索分段
```
table.search(limit=10, offset=0, **{"字段1" : "数据"})
```

## 其他操作
### 关闭连接
```
del table
```

### 获取所有库名
```
table.dbs
```

### 获取该库下所有collection
```
table.tables
```

### 获取所有字段名
```
table.colums
```

### 关闭日志
```
table.none_log()
```

### 开启日志
```
table.en_log()
```
"""

LONG_DESCRIPTION = read("README.md")

setup(
    name = "pymongos",
    version = "1.1.9"
    ,
    description = "use MongoDB just like json.",
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = "MongoDB simple dict json",
    author = "e4ting",
    author_email = "e4tingcom@gmail.com",
    url = "https://github.com/77409/pymongos",
    license = "MIT",
    py_modules = ["pymongos", ],
    install_requires=["pymongo",],
    include_package_data=True,
    zip_safe=True,
)
