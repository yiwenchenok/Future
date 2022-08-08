from celery import Celery
from .celeryconfig import Config

app = Celery("c_test")

# 加载配置
app.config_from_object(Config)

# 自动发现任务
app.autodiscover_tasks(["celery_test"])
