===================
pymongos
===================
简化了一些`pymongo`的操作，像操作`dict`一样操作你的数据。
因为日常用增删查改最多，所以简化主要是围绕这三个操作来的。

===================
安装
===================
code
::
    python -m pip install pymongos
    python3 -m pip install pymongos


===================
连接数据库
===================

-   无密码连接
code
::
    from pymongos import mongodb
    table = mongodb(host='127.0.0.1', db="test", table="test")
    # 无日志
    table = mongodb(host='127.0.0.1', db="test", table="test", level="debug")

-   密码连接
code
::
        from pymongos import mongodb
        table = mongodb(host='127.0.0.1', db="test", table="test", user="admin", passwd="123456789")

===================
插入数据
===================

-   不设置_id（MongoDB随机生成）
    code
    ::
        table += {"字段1": "数据1", "字段2": "数据1"}
    or
    ::
        table + {"字段1": "数据1", "字段2": "数据1"}

    因为分配的ID是随机的，不建议使用

-   设置_id
    code
    ::
        table["设置_id"] = {"字段1": "数据3", "字段2": "数据4"}
        table["test"] = {"爱好": "看书", "书名": "鬼吹灯"}


===================
删除数据
===================

-   仅支持指定key方式
code::
    del table["设置_id"]


===================
修改
===================
code::
    table["test"] = {"书名": "鬼吹灯和三体"}
    table["test"] = {"书名": "《鬼吹灯》《三体》", "爱好": "看书&游泳"}
    table["test"] = {"name" : "e4ting"}

===================
取数据
===================

-   表长度
    code::
        len(table)


-   _id是否存在
    code::
        if "test" in table:
            print("yes")


-   获取所有_id
    code::
        table.keys()

-   根据_id取
    code::
        data = table["test"]
        print(data)


-   取整个表数据
    数据少的时候才可以这么豪横的用
    code::
        table.get()


-   遍历表
    表太大的时候，迭代取
    code::
        for _ in table:
            print(_)


-   过滤
    code::
        table.get(name="e4ting")
        table.get(**{"字段1":"数据1"})


-   分段
    code::
        table.get(limit=10, offset=1)

-   搜索
    code::
        table.search(name="4ting")

-   搜索分段
    code::
        table.search(limit=10, offset=0, **{"字段1" : "数据"})


===================
其他操作
===================
-   关闭连接
    code::
        del table


-   获取所有库名
    code::
        table.dbs


-   获取该库下所有collection
    code::
        table.tables


-   获取所有字段名
    code::
        table.colums


-   关闭日志
    code::
        table.none_log()


-   开启日志
    code::
        table.en_log()

