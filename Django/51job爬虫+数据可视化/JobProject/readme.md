#### 安装教程

1. 安装依赖 pip install -r requirements.txt

### 数据库配置

- mysql配置需要修改setting.py中的DATABASES
- 执行数据表创建
- python manage.py migrate

#### 使用说明

1.分别运行数据爬虫入库教程
- 需要先获取cookie
- 首先运行JobScript/spider.py 里面设置爬取内容和数量
- 运行JobScript/cleaning_data.py 进行数据清洗
- 运行JobScript/import_data.py 数据入库

2.或者一起运行

- 运行JobScript/run.py

3.创建管理员

- python manage.py createsuperuser
- 127.0.0.1:8000/admin 后台管理界面

4.启动服务

- python manage.py runserver