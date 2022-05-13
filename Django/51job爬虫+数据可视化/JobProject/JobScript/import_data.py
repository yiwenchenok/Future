import sys
import os
import django
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.update({"DJANGO_SETTINGS_MODULE": "JobProject.settings"})
django.setup()

from job.models import JobInfo


def run(file_path='job_clearing_result.xlsx'):
    df = pd.read_excel(file_path, engine='openpyxl')
    for item in df.iterrows():
        job_t_dict = item[1]
        JobInfo.objects.get_or_create(**job_t_dict)
    print('import success')


if __name__ == '__main__':
    run()
