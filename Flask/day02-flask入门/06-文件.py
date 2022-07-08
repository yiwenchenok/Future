# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/19 21:23
# File:05-文件
import hashlib
import time
import uuid
from flask import Flask,request


app = Flask(__name__)

@app.route("/upload",methods=['get','post'])
def upload():
    f = request.files.get("pic")
    #todo；方法1
    #避免非法字符造成保存失败
    # has = hashlib.md5()
    # has.update(f.filename.encode("utf-8"))
    # filename = has.hexdigest()
    # f.save(f"{filename}{time.time()}.png")

    #todo;方法2
    filename = uuid.uuid4()
    f.save(f"{filename}.png".replace("-",""))

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)