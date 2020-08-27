# pymongos
    简化了一些`pymongo`的操作，像操作`dict`一样操作你的数据

## 安装
### 先装依赖
```
git clone 
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
```
table += {""}
```

