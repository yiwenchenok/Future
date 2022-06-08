#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 03-xpath语法.py

from lxml import etree


html = """
<dd>
                        <i class="board-index board-index-9">9</i>
    <a href="/films/1303" title="美丽人生" class="image-link" data-act="boarditem-click" data-val="{movieId:1303}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default">
      <img alt="美丽人生" class="board-img" src="https://p1.meituan.net/movie/580d81a2c78bf204f45323ddb4244b6c6821175.jpg@160w_220h_1e_1c">
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1303" title="美丽人生" data-act="boarditem-click" data-val="{movieId:1303}">美丽人生</a></p>
        <p class="star">
                主演：罗伯托·贝尼尼,朱斯蒂诺·杜拉诺,赛尔乔·比尼·布斯特里克
        </p>
        <p class="releasetime">上映时间：2020-01-03</p>  
  </div>
    <div class="movie-item-number score-num">
            <p class="score"><i class="integer">9.</i><i class="fraction">3</i></p>        
    </div>

      </div>
    </div>

                </dd>
"""


selector = etree.HTML(html) #序列化html
name = selector.xpath("//p[@class='name']//@href")  #获取属性值
name_text = selector.xpath("//p[@class='name']//text()")  #获取标签文本
print(name)
print(name_text)

p_all = selector.xpath('//p[last()]//i/text()')
print(''.join(p_all))




