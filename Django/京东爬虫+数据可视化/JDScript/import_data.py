import sys
import os
import django
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.update({"DJANGO_SETTINGS_MODULE": "JDProject.settings"})
django.setup()

from app.models import JDProductData


def run(file_path='clearing_result.xlsx'):
    df = pd.read_excel(file_path, engine='openpyxl')
    for item in df.iterrows():
        product_dict = item[1]
        JDProductData.objects.get_or_create(**product_dict)
    print('success')


if __name__ == '__main__':
    run()
