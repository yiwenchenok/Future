# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from application import app
import re, json
from common.libs.UploadService import UploadService
from common.libs.UrlManager import UrlManager  # 图片绝对地址
from web.models.Image import Image

route_upload = Blueprint('upload_page', __name__)
'''
参考文章：https://segmentfault.com/a/1190000002429055
上传的逻辑。。。
'''


@route_upload.route("/ueditor", methods=["GET", "POST"])
def ueditor():
    """
	上传一定时post，获取请求一定是get，这里是完成富文本编辑器Ueditor中的上传逻辑
	:return:
	"""
    req = request.values
    action = req['action'] if 'action' in req else ''
    if action == "config":  # 返回json对象
        root_path = app.root_path
        config_path = "{0}/web/static/plugins/ueditor/upload_config.json".format(root_path)
        with open(config_path, encoding="utf-8") as fp:
            try:
                config_data = json.loads(re.sub(r'\/\*.*\*/', '', fp.read()))  # /*注释去掉，把json中备注去掉，因为json中的注释不能自动识别注释
            except:
                config_data = {}
        return jsonify(config_data)
    if action == "uploadimage": #上传图片
        return uploadImage()
    if action == "listimage":  # 富文本编辑器中的在线管理功能，返回已经上传的图片
        return listImage()
    return "upload"


def uploadImage():
    resp = {'state': 'SUCCESS', 'url': '', 'title': '', 'original': ''}
    file_target = request.files  # 取出文件
    upfile = file_target['upfile'] if 'upfile' in file_target else None
    if upfile is None:
        resp['state'] = "上传失败"
        return jsonify(resp)
    ret = UploadService.uploadByFile(upfile)  # 有图片就上传，上传的动作比较通用，用统一的上传类
    if ret['code'] != 200:
        resp['state'] = "上传失败：" + ret['msg']
        return jsonify(resp)
    resp['url'] = UrlManager.buildImageUrl(ret['data']['file_key'])
    return jsonify(resp)


def listImage():#用于富文本编辑器的图片上传中的在线管理功能
    # 图片展示的效果
    resp = {'state': 'SUCCESS', 'list': [], 'start': 0, 'total': 0}
    req = request.values  # ueditor富文本编辑器内部封装了请求，会传这个start到后端
    start = int(req['start']) if 'start' in req else 0
    page_size = int(req['size']) if 'size' in req else 20
    # 分页
    query = Image.query
    if start > 0:  # 倒序排列的，第一次查询的时候start为0，通过id去取数据，实现分页。数据库优化常用功能
        query = query.filter(Image.id < start)
    list = query.order_by(Image.id.desc()).limit(page_size).all()  # 根据id倒序排列
    images = []
    if list:
        for item in list:
            images.append({'url': UrlManager.buildImageUrl(item.file_key)})
            start = item.id
    resp['list'] = images #将图片的路径封装在list里面，传递给页面
    resp['start'] = start  # start值更新
    resp['total'] = len(images) #将图片的最大数目封装在total里面，传递给页面
    return jsonify(resp)


@route_upload.route("/pic", methods=["GET", "POST"])
def uploadPic():
    """上传封面"""  # js中写change触发就实现submit，构建一个irame隐藏域，将form表单中的target指向iframe中的name,刷新上传就实现了
    file_target = request.files
    upfile = file_target['pic'] if 'pic' in file_target else None
    callback_target = 'window.parent.upload'
    if upfile is None:
        return "<script type='text/javascript'>{0}.error('{1}')</script>".format(callback_target, "上传失败")
    ret = UploadService.uploadByFile(upfile)  # 上传封面和Ueditor中的图片上传的逻辑一样
    if ret['code'] != 200:
        return "<script type='text/javascript'>{0}.error('{1}')</script>".format(callback_target, "上传失败：" + ret['msg'])
    return "<script type='text/javascript'>{0}.success('{1}')</script>".format(callback_target, ret['data']['file_key'])
# ret['data']['file_key']：照片路徑
