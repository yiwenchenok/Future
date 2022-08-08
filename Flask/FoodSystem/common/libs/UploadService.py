# -*- coding: utf-8 -*-
from werkzeug.utils import secure_filename
from pypinyin import lazy_pinyin
from application import app,db
from common.libs.Helper import getCurrentDate
import datetime
import os,stat,uuid #通用唯一标识符 ( Universally Unique Identifier ),
from web.models.Image import Image

class UploadService():
	@staticmethod
	def uploadByFile(file):
		resp = { 'code':200,'msg':'操作成功~~','data':{} }
		# secure_filename:函数获得安全文件名,防止客户端伪造文件,全中文是不支持的.
		# 通过lazy_pinyin 将文件中文转拼音，才能通过secure_filename方法
		filename = secure_filename(''.join(lazy_pinyin(file.filename)))
		ext = filename.rsplit(".",1)[1]
		if ext not in app.config['UPLOAD']['ext']:#获取配置文件中UPLOAD字典里面的ext字段的数据
			resp['code'] = -1
			resp['msg'] = "不允许的扩展类型文件"
			return resp
		root_path = app.root_path + app.config['UPLOAD']['prefix_path']#获取配置文件中UPLOAD字典里面的prefix_path字段的数据
		#不使用getCurrentDate创建目录，为了保证其他写的可以用，这里改掉，服务器上对时间不兼容
		#file_dir为储存上传照片的文件目录名，以每天的方式储存
		file_dir = datetime.datetime.now().strftime("%Y%m%d")  #.strftime("%Y%m%d")定义一个日期的字条串
		save_dir = root_path + file_dir
		if not os.path.exists( save_dir ):
			os.mkdir( save_dir )
			#赋予权限
			#stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
			#stat.S_IRGRP: 组用户有读权限0o040
			#stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
			os.chmod(save_dir,stat.S_IRWXU|stat.S_IRGRP|stat.S_IRWXO)#os.chmod()方法用于更改文件或目录的权限。
		#UUID: 通用唯一标识符 ( Universally Unique Identifier ),
		# 对于所有的UUID它可以保证在空间和时间上的唯一性. 它是通过MAC地址,
		# 时间戳, 命名空间, 随机数, 伪随机数来保证生成ID的唯一性, 有着固定的大小( 128 bit ).
		file_name = str( uuid.uuid4() ).replace("-","") + "." + ext
		file.save("{0}/{1}".format(save_dir,file_name)) #文件保存到指定路径
		model_image = Image()
		model_image.file_key = file_dir + "/" + file_name  #保存在数据库中的数据路径 时间/file_name,每天会创建以时间命名新的文件夹
		model_image.created_time = getCurrentDate()
		db.session.add(model_image)
		db.session.commit()

		resp['data'] = {
			'file_key': model_image.file_key
		}
		return resp