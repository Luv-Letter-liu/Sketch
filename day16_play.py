# import pymysql
# db = pymysql.connect(host = 'localhost',
#                     port = 3306,
#                     user = 'root',
#                     password = '123456',
#                     database = 'stu',
#                     charset = 'utf8')
# cur = db.cursor()
#
# try:
#     name = input('Name:')
#     age = input('Age:')
#     sex = input('Sex:')
#     score = input('Score:')
#     sql = "insert into class1 (name,age,sex,score)\
#           values (%s,%s,%s,%s);"
#     cur.execute(sql,[name,age,sex,score])
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
#
# cur.close()
# db.close()
# 不醉不会--田馥甄~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import pymysql
# db = pymysql.connect(host = 'localhost',
#                     port = 3306,
#                     user = 'root',
#                     password = '123456',
#                     database = 'stu',
#                     charset = 'utf8')
# cur = db.cursor()
#
# try:
#     sql = "update class1 set sex = 'm' where name = 'siri';"
#     cur.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
#
# cur.close()
# db.close()
# 谁无聊拿放大镜 看风景累不累~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import pymysql
# db = pymysql.connect(host = 'localhost',
#                     port = 3306,
#                     user = 'root',
#                     password = '123456',
#                     database = 'stu',
#                     charset = 'utf8')
# cur = db.cursor()
#
# try:
#     exe = []
#     for i in range(3):
#         name = input('Name:')
#         age = input('Age:')
#         sex = input('Sex:')
#         score = input('Score:')
#         exe.append((name,age,sex,score))
#     sql = "insert into class1 (name,age,sex,score)\
#           values (%s,%s,%s,%s);"
#     cur.executemany(sql,exe)
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
#
# cur.close()
# db.close()
# 却忘记了看清楚 自己是谁~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import pymysql
# db = pymysql.connect(host = 'localhost',
#                     port = 3306,
#                     user = 'root',
#                     password = '123456',
#                     database = 'dict',
#                     charset = 'utf8')
# cur = db.cursor()
#
# f = open('dict.txt','r')
# exe = []
# for item in f:
#     word = item.split(' ')[0]
#     mean = item.split(' ',1)[1]
#     exe.append((word,mean))
# try:
#     sql = "insert into words (word,mean)\
#           values (%s,%s);"
#     cur.executemany(sql,exe)
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
# cur.close()
# db.close()
# 我的宇宙轻飘飘　美得摇摇欲坠~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import pymysql
# db = pymysql.connect(host = 'localhost',
#                     port = 3306,
#                     user = 'root',
#                     password = '123456',
#                     database = 'stu',
#                     charset = 'utf8')
# cur = db.cursor()
#
# sql = 'select name from class1 where score > 80;'
#
# cur.execute(sql)
# print(cur.fetchall())
#
# cur.close()
# db.close()
# 旁人来来去去像行云流水 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import pymysql
# db = pymysql.connect(host = 'localhost',
#                     port = 3306,
#                     user = 'root',
#                     password = '123456',
#                     database = 'stu',
#                     charset = 'utf8')
# cur = db.cursor()
#
#
# # with open('1.png','rb') as f:
# #     data  =f.read()
# # try:
# #     sql = 'update class1 set img = %s where name = "小哀";'
# #     cur.execute(sql,[data])
# #     db.commit()
# # except:
# #     db.rollback()
#
# sql = 'select img from class1 where name = "小哀";'
# cur.execute(sql)
# data = cur.fetchone()
# with open('小哀.png','wb') as f:
#     f.write(data[0])
#
#
# cur.close()
# db.close()
# 模糊糊的视线不管天色黑不黑~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import pymysql
# class Database:
#     def __init__(self):
#         self.db = pymysql.connect(host = 'localhost',
#                                   port = 3306,
#                                   user = 'root',
#                                   password = '123456',
#                                   database = 'stu',
#                                   charset = 'utf8')
#         self.cur = self.db.cursor()
#
#     def register(self,name,passwd):
#         sql = 'select name from user where name = "%s";'%name
#         self.cur.execute(sql)
#         result = self.cur.fetchone()
#         if result:
#             return False
#         try:
#             sql = 'interest into user (name,passwd) values (%s,%s)'
#             self.cur.execute(sql,[name,passwd])
#             self.db.commit()
#             return True
#         except:
#             self.db.rollback()
#             return False
#     def login(self,name,passwd):
#         sql = "select name,passwd from user \
#               where name = %s and passwd = %s"
#         self.cur.execute(sql,[name,passwd])
#         result = self.cur.fetchone()
#         if result:
#             return True
# if __name__ == '__main__':
#     db = Database()
#     print(db.login('yasuo','0210'))
# 心中没鬼就不用处处防备~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pymysql


class Database:
    def __init__(self,name,passwd):
        self.db = pymysql.connect(host = 'localhost',
                                  port = 3306,
                                  user = 'root',
                                  password = '123456',
                                  database = 'stu',
                                  charset = 'utf8')
        self.cur = self.db.cursor()
    def register(self,name,passwd):
        sql = 'select name from user where name = "%s"'%name
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return False
        try:
            sql = 'insert into user(name,passwd) values (%s,%s)'
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def login(self,name,passwd):
        sql = 'select name,passwd from user \
              where name = %s and passwd = %s'
        self.cur.execute(sql,[name,passwd])
        result = self.cur.fetchone()
        if result:
            return True
if __name__ == '__main__':
    db = Database()
    print(db.login('Lily','1234'))