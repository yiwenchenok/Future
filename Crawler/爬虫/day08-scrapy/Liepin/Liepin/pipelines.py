# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import pymysql # pip install pymysql
class LiepinPipeline:
    def __init__(self):
        self.f = open("liepin3.csv",'a',newline="",encoding='utf8')
        lis = ["title",'link','company','money','addr','age','edu']
        self.writer = csv.DictWriter(self.f,fieldnames=lis)
        self.writer.writeheader() #写入表头
    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self,spider):
        self.f.close()

class LiepinMysqlPipline():
    def __init__(self):
        #连接mysql
        self.user = "root"
        self.password = "mysql"
        self.host = "127.0.0.1"
        self.port = 3306
        self.db_name = "liepin"
        self.chase = 'utf8'
        self.table_name = "py25_spider"
        self.db = pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            db=self.db_name,
            charset=self.chase)
        self.cursor = self.db.cursor()

        #创建表
        try:
            sql = f"""
            CREATE TABLE `{self.table_name}` (
              `id` int(11) NOT NULL AUTO_INCREMENT,
              `title` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '职位名称',
              `link` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '链接',
              `company` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '公司',
              `money` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '薪资',
              `addr` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '公司地址',
              `edu` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '教育程度',
              `age` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '经验',
              PRIMARY KEY (`id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
            """

            self.cursor.execute(sql)
            self.db.commit()

        except Exception as e:
            print("表已经存在",e)


    def process_item(self, item, spider):
        try:
            insert_sql = f"""
            insert into {self.table_name}(title,link,company,money,addr,edu,age) values (%s,%s,%s,%s,%s,%s,%s)
            """
            self.cursor.execute(insert_sql,( item["title"],item["link"],item["company"],item["money"],item["addr"],item["edu"],item["age"]))
            self.db.commit()
        except:
            pass


    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()




