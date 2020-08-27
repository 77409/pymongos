# pymongos
    简化了一些`pymongo`的操作，像操作`dict`一样操作你的数据

## 安装
### 先装依赖
```
git clone https://github.com/77409/pymongos.git

python -m pip install pymongo
```
或者
```
python -m pip install -r requirments.txt
```
> `requirments.txt`还没上传

### 再装本模块
```
git clone 
```

## 连接数据库

### 无密码连接
```
from pymongos import mongodb
table = mongodb(host='127.0.0.1', db="test", table="test")
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
```
