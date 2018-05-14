import pymysql
class DB():
    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PWD, DB_NAME):
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DB_USER = DB_USER
        self.DB_PWD = DB_PWD
        self.DB_NAME = DB_NAME

        self.conn = self.getConnection()

    #连接
    def getConnection(self):
        return pymysql.Connect(
            host=self.DB_HOST,  #设置MYSQL地址
            port=self.DB_PORT,  #设置端口号
            user=self.DB_USER,  #设置用户名
            passwd=self.DB_PWD, #设置密码
            db=self.DB_NAME,    #设置数据库名
            charset='utf8'      #设置编码
        )