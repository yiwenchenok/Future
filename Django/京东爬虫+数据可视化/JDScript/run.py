from JDScript.spider import run as spliter_run
from cleaning_data import run as clearing_run
from import_data import run as import_run


def run():
    print('开始获取数据')
    spliter_run(search_name='飞机杯', max_count=10, file_name='result.xlsx')
    print('开始清洗数据')
    clearing_run()
    print('开始入库')
    import_run()


if __name__ == '__main__':
    run()
