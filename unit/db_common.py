# coding:utf-8
import pymysql

from unit.common import ReadConfig
from unit.logger import Logger


class DbOption(object):
    def __init__(self):
        self.cf = ReadConfig()
        self.host = self.cf.get_database_data("host")
        self.username = self.cf.get_database_data("username")
        self.password = self.cf.get_database_data("password")
        self.port = int(self.cf.get_database_data("port"))
        self.basename = self.cf.get_database_data("basename")
        self.mylogger = Logger("connect_db").get_log()
        self.conn = None

    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host,user=self.username,passwd=self.password,db=self.basename,port=self.port,charset='utf8')

        except Exception as msg:
            pass
            self.mylogger.info("数据库连接错误：{0}".format(msg))
        return self.conn

    def select(self,sql):
        cursor  = self.connect().cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as msg:
            self.mylogger.info("sql查询错误：{0}".format(msg)+"\n" + "错误sql:{0}".format(sql))
            data = ()
        cursor.close()
        self.conn.close()
        return data

    def operation(self,sql):
        cursor = self.connect().cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
        except Exception as msg:
            self.conn.rollback()
            self.mylogger.info("sql:{0} 操作失败：{1}".format(msg,sql))
        cursor.close()
        self.conn.close()

if __name__ == "__main__":
    sql = "SELECT id FROM bt_course_grouping where id =10000 "
    d = DbOption().select(sql)
    # print(d)

