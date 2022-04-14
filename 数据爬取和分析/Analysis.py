from my_sqlite import *
from get_infor import open_url
from bs4 import BeautifulSoup
import translation as t
import pandas as pd
import numpy as np
from pyecharts.charts import Liquid, Pie,Bar,Map,Boxplot,Page,WordCloud
import pyecharts.options as opts
import warnings
from pyecharts.globals import ThemeType
import jieba
from snownlp import SnowNLP

def get_url(res):
    # 将网页源码转换成标签树形式
    soup = BeautifulSoup(res, "lxml")
    source = soup.find_all('div', class_="wysiwyg wysiwyg--all-content css-1at35hh")
    result = []
    for each in source:
        for e in each.select("p"):
            if e.text.strip() :
                result.append(t.translate(e.text))
    with open("data\china.txt",'w',encoding='utf8') as f:
        for each in result:
            f.write(each)

    return result

def snow(result):
    sentimentslist = []
    count = 0
    for i in result:
        s = SnowNLP(i)
        if s.sentiments > 0.5:
            count += 1
        sentimentslist.append(s.sentiments)

    sentimentslist = [round(e, 2) for e in sentimentslist]
    data = pd.DataFrame({'c': sentimentslist})
    date = pd.DataFrame(data.value_counts())
    dict_date = {'x': [e[0] for e in date.index], 'y': [e[0] for e in date.values]}
    df_date = pd.DataFrame(dict_date)
    # df_date.sort_index(level='x', inplace=True,ascending=False)
    df_date.sort_values(by='x', inplace=True)

    # dic_sentimentslist = dict(zip())



    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            .add_xaxis(list(df_date['x']))
            .add_yaxis("Quantity", list(df_date['y']))
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(name='Sentiments Probability', axislabel_opts=opts.LabelOpts(rotate=-45)),
            title_opts=opts.TitleOpts(title="Analysis of Sentiments"))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    bar.render('html\Analysis of Sentiments.html')

    liquid = Liquid()
    liquid.add('', [count/len(result)])
    liquid.set_global_opts(title_opts=opts.TitleOpts(title="正面占比"))
    liquid.render('html\正面占比.html')
def cut(result,title):
    stopwords_file = open('data\stopword.txt', 'r', encoding='utf-8')
    stopwords = [words.strip() for words in stopwords_file.readlines()]
    words = ' '.join(result)
    dic_word = {}
    title_word = []

    for word in jieba.cut(words):
        if word.strip() not in dic_word and word not in stopwords:
            dic_word[word] = 1
        elif word.strip() in dic_word and word not in stopwords:
            dic_word[word] += 1
    dic_word = sorted(dic_word.items(),key=lambda item:item[1],reverse=True)
    for word in jieba.cut(title):
        if word not in title_word and word not in stopwords:
            title_word.append(word)
    print(dic_word[:10])
    print(title_word)
    num = sum([e[1] for e in dic_word[:10]])
    count = 0
    for e in dic_word[:10]:
        if e[0] in title_word:
            count += e[1]
    liquid = Liquid()
    liquid.add('', [count / num])
    liquid.set_global_opts(title_opts=opts.TitleOpts(title="正面占比"))
    liquid.render('html\关联程度.html')

def main():
    results = select()
    res = open_url(results[0][1])
    result = get_url(res)
    snow(result)
    cut(result,results[0][0])
main()
