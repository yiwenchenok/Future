from .celery import app


@app.task
def task1(a, b):
    print("task1")
    return a + b


@app.task
def task2(a, b):
    print("task2")
    return a + b


@app.task
def task3(a, b):
    print("task3")
    return a + b


@app.task
def task4(a, b):
    print("task4")
    return a + b


@app.task
def upload_img():
    print("upload_img 任务函数正在执行....")


@app.task
def handle_img():
    print("handel_img 任务函数正在执行....")


@app.task
def send_message():
    print("send_message 任务函数正在执行....")
