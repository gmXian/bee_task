# -*- coding: utf-8 -*-
"""
作者：XGM
日期：2021年05月20日11时03分33秒
"""

import requests
url="https://www.jd.com/"
response=requests.get(url=url)
page_text=response.text
with open('./jd.html','w',encoding='utf-8')as fp:
    fp.write(page_text)
print("爬取数据结束！")