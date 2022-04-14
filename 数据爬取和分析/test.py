#import pymysql
import pymysql


def connect():
    # 建立连接
    db = pymysql.connect(host='localhost',user='root',password='root',port=3306)
    # 使用 cursor() 方法创建游标对象 cursor，利用游标来执行SQL语句
    cursor = db.cursor()

    # SQL执行创建数据库的操作，数据库名叫做 employ，默认编码UTF-8
    sql = 'CREATE DATABASE employ DEFAULT CHARACTER SET utf8'
    cursor.execute(sql)

    print("Database terminate was created successfully")

    db.close()

def create_table():
    # 建立连接和游标
    db = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='employ')
    cursor = db.cursor()

    try:
        cursor.execute('''CREATE TABLE infor
                 (title VARCHAR(255) PRIMARY KEY NOT NULL,
                 url TEXT);''')
          #print("Table created successfully")
    except:
        cursor.execute('drop table infor')
        cursor.execute('''CREATE TABLE infor
                               (title VARCHAR(255) PRIMARY KEY NOT NULL,
                               url TEXT);''')
          #print("Table created successfully")

    print("Data table created successfully")

    # 关闭连接
    db.close()

def  insert(result):
    db = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='employ')
    cursor = db.cursor()

    sql = "insert into infor (title,url)  values (%s, %s)"

    for each in result:
        data = (each[1],each[0])

        try:
            cursor.execute(sql,data)
            db.commit() # 需要执行db对象的commit() 方法才可实现数据插入
    
        except Exception as e:
            print("FAILED!",e)
            db.rollback() # 回滚
    print("Ok!")
    cursor.close()
    db.close()

#查找数据
def select():
    db = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='employ')
    cursor = db.cursor()
    print("Opened database successfully")
    sql = 'SELECT * from infor'
    cursor.execute(sql)
    results = cursor.fetchall()
     
    cursor.close()
    db.close()

    return results
