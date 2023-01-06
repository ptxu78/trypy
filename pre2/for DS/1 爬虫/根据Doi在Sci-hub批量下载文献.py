# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:48:33 2021
@author: rwh
"""
import requests
from bs4 import BeautifulSoup
import os

Title = []
# 将Doi文件的地址放在这里-最好手输，不要复制粘贴
f = open(r"D:\专题三英文文献标题.txt", encoding="utf-8");
for line in f.readlines():
    line = line[:-1]
    Title.append(line)
Title = Title[1:-1]
# 将下载文件的存储地址放在这里-最好手输，不要复制粘贴
path = "D:\专题三英文文献"
if os.path.exists(path) == False:
    os.mkdir(path)
# 将自己电脑的user-agent输入，具体方法可以百度查询
head = {\
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'\
    }

for title in Title:
    try:
        url = "https://sci-hub.ren/" + title
        print(url)
        r = requests.get(url, headers=head)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "html.parser")
        download_url = soup.iframe.attrs["src"]  # 20210515更新
        print(title + " is downloading...\n  --The download url is: " + download_url)
        download_r = requests.get(download_url, headers=head)
        download_r.raise_for_status()
        f = open(path + "/" + title.replace("/", "_") + ".pdf", "wb")
        f.write(download_r.content)
    except:
        print("我没下载好!!\t" + title)
