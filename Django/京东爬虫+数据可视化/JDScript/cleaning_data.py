# 数据清洗
import json
import pandas as pd
import os


def get_gender(val):
    """获取性别"""
    data_list = json.loads(val)
    for d in data_list:
        gender = d.get('适用性别', '')
        if gender:
            return gender
    return '未知'


def convert_sale(val):
    """对评价数据进行转换和保存"""
    tem = val.split('+')[0]
    if '万' in tem:
        sale = int(tem.split('万')[0]) * 10000
    else:
        sale = int(tem)
    return sale


def cleaning_data(file_path: str):
    """
    清洗数据
    :param file_path:  文件名
    :return: 清洗后的文件
    """
    df = pd.read_excel(file_path, engine='openpyxl')
    # 数据去重 商品id唯一,可以用来判重
    dup_df = df.drop_duplicates(subset=['product_id'], keep='first')
    dup_df['p_price'].astype('float')

    # 删除缺失值
    dup_df = dup_df.dropna()

    # 新增一列性别的列 对缺失值设置未知
    dup_df['p_gender'] = dup_df['p_detail'].apply(get_gender)

    # 对销量数据进行转换，把字符串改为int类型
    dup_df['p_sale'] = dup_df['p_comment_count'].apply(convert_sale)

    dup_df.to_excel(f'clearing_result.xlsx', index=False)


def run(file='result.xlsx'):
    cleaning_data(file)


if __name__ == '__main__':
    run()
