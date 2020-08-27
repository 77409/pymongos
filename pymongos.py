#!/bin/env python
# -*- coding:utf-8 -*-

import pymongo
import logging
import json
import os
from pdb        import set_trace  as strace
from traceback  import format_exc as dumpstack

pid = os.getpid()

logging.basicConfig(level=logging.INFO, format="[%(asctime)s][pid:%(process)d %(levelname)s] %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()

def log(*args, level='info'):
    log_func = getattr(logger, level)
    log_func("{: ^10}: {}".format(traceback.extract_stack()[-2][2], " ".join([str(_) for _ in args])))

class mongodb(object):
    def __init__(self, **kwargs):
        self.host = "mongo.com"
        self.port = 27017
        self.user = None
        self.passwd = None
        self.db   = "data"
        self.table= "test"
        self.conn = None
        self.cur  = None
        self.level = "info"
        self.is_login = False
        self.mechanism = "SCRAM-SHA-1"
        [setattr(self, k, v) for k,v in kwargs.items()]
        # self.login()

    def none_log(self):
        self.level = "debug"

    def en_log(self, level='info'):
        self.level = level

    @property
    def dbs(self):
        """ 获取所有数据库名 """
        self.login()
        return self.conn.list_database_names()

    @property
    def tables(self):
        """ 获取数据库的所有表名 """
        self.login()
        return self._db.list_collection_names()

    @property
    def colums(self):
        self.login()
        return self._table.find_one().keys()

    def get_db_tables(self, db):
        self.login()
        return self.conn[db].list_collection_names()

    def login(self):
        if self.is_login:
            return True
        self.conn = pymongo.MongoClient("mongodb://{host}:{port}/".format(**self.__dict__))
        if self.user and self.passwd:
            auth = self.conn["admin"]
            auth.authenticate(self.user, self.passwd, mechanism=self.mechanism)
        self._db = self.conn[self.db]
        self._table = self._db[self.table]
        self.is_login = True
        return True

    def __repr__(self):
        return "mongodb://{host}:{port}/{db}/{table}".format( **self.__dict__)

    def __del__(self):
        if self.conn: self.conn.close()

    def format(self, data):
        ret = { k: json.dumps(v) if type(v) in [list, dict] else v for k, v in data.items()}
        return ret

    def keys(self, **kwargs):
        self.login()
        data = self._table.find(kwargs, { "_id": 1})
        return [ _["_id"] for _ in data ]

    def __iter__(self):
        self.login()
        return self._table.find({}, no_cursor_timeout = True).batch_size(200)

    # 两种迭代方式，其实我更喜欢下面这种，上面的更优雅
    # def __iter__(self):
    #     self._t_iter = self._table.find({})
    #     return self

    # def __next__(self):
    #     return next(self._t_iter)

    def get(self, limit=False, offset=0, _cols_={}, order=None, desc=False, **kwargs):

        self.login()
        if _cols_:
            data = self._table.find(kwargs, _cols_)
        else:
            data = self._table.find(kwargs)
        if order:
            data = data.sort(order, -1 if desc else 1)
        if limit:
            data = data.limit(limit)
        if offset:
            data = data.skip(offset)
        return [ _ for _ in data ]

    def search(self, limit=False, offset=0, _cols_={}, **kwargs):
        self.login()
        def __(kwargs):
            return { filed :{'$regex': keyword} for filed,keyword in kwargs.items() }

        if not limit:
            # data = self._table.find(kwargs, _cols_).skip(offset)
            data = self._table.find(__(kwargs)).skip(offset)
        else:
            # data = self._table.find(kwargs, _cols_).limit(limit).skip(offset)
            data = self._table.find(__(kwargs)).limit(limit).skip(offset)
        return [ _ for _ in data ]

    def len_search(self, **kwargs):
        self.login()
        return self._table.find(kwargs).count()

    def __len__(self):
        self.login()
        return self._table.count()

    def count(self, **kwargs):
        self.login()
        return self._table.count_documents(kwargs)

    def __delitem__(self, _id):
        log(str(self), "删除", _id, level=self.level)
        self.login()
        return self._table.delete_one({"_id":_id})

    def __setitem__(self, _id, item):
        if not _id in self:
            item["_id"] = _id
            return self + item
        if "_id" in item : del item["_id"]
        data = self.format(item)
        log(str(self), "修改", _id, data, level=self.level)
        self.login()
        self._table.update_one({"_id":_id}, {"$set":item})

    def clearall(self):
        log("清空 {}".format(str(self)))
        self.login()
        return self._table.remove({})

    def __contains__(self, _id):
        return bool(self[_id])

    def __getitem__(self, _id):
        self.login()
        data = self._table.find({"_id":_id})
        # strace()
        if data.count() <= 0:
            return None
        return [_ for _ in data][0]

    def __add__(self, item):
        data = self.format(item)
        log(str(self), "新增", data, level=self.level)
        self.login()
        self._table.insert_one(item)
        return self

    def __iadd__(self , item):
        return self + item
