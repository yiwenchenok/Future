class Config:
    broker_url = "redis://127.0.0.1:6379/6",
    result_backend = "redis://127.0.0.1:6379/7"

    #任务路由
    task_routes = ({
                       'celery_test.tasks.upload_img': {'queue': 'img_queue'},
                       'celery_test.tasks.handle_img': {'queue': 'img_queue'},
                       'celery_test.tasks.send_message': {'queue': 'send_queue'},
                   },
    )

# celery -A celery_test worker -l info --pool=solo

#指定队列启动worker
#celery -A celery_test  worker -l info -Q myqueque --pool=solo


#celery -A celery_test  worker -l info -Q img_queue,send_queue --beat

