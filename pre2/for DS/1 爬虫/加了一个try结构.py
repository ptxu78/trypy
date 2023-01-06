
import requests
from bs4 import BeautifulSoup
import os

DOI = []
# 将Doi文件的地址放在这里-最好手输，不要复制粘贴
f = open(r"Doi1.txt", encoding="utf-8");
for line in f.readlines():
    line = line[:-1]
    DOI.append(line)
DOI = DOI[1:-1]
# 将下载文件的存储地址放在这里-最好手输，不要复制粘贴
path = "秦政1"
if os.path.exists(path) == False:
    os.mkdir(path)
# 将自己电脑的user-agent输入，具体方法可以百度查询
head = {\
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'\
    }

for doi in DOI:
    try:
        url = "https://sci-hub.ren/" + doi
        print(url)
        r = requests.get(url, headers=head)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "html.parser")
        download_url = soup.iframe.attrs["src"]  # 20210515更新
        print(doi + " is downloading...\n  --The download url is: " + download_url)
        download_r = requests.get(download_url, headers=head)
        download_r.raise_for_status()
        f = open(path + "/" + doi.replace("/", "_") + ".pdf", "wb")
        f.write(download_r.content)
    except:
        print("我没下载好!!\t" + doi)
