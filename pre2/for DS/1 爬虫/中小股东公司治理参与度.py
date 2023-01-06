import json

import requests

#数据列表的地址
stock_data_url='http://ww.cn1nfo.com.cn/neu/fulltextsearch/full?searchkey-aEsuB9qB4@E6U8AsASSsdate=&edate-G1sfulltext=faLseGsortNane-pubdatessortType=descpageNum=1'
#PDF文件的地址前缀
pdf_bes1c_url='http://static.cninfo.com.cn/'

#使用request进行网络请求
r = requests.get(url=stock_data_url)

print(r)
print(r.json)

data=json.loads(r.text).get('announcements')

print(data)
print(len(data))

#将每一行的数据循环下载
for i in range(0,len(data)):
    secCode=data[i].get('secCode')
    print(secCode)
    secName=data[i].get('secName')
    print(secName)
    announcementTitle = data[i].get('announcement')
    announcementTitle=announcementTitle.replace('<em>','').replace('</em','')#将html标签<em>,</em>替换为空
    print(announcementTitle)
    pdfUrl=data[i].get('adjunctUrl')
    print(pdfUrl)
    pdfFullUrl=pdf_basic_url+pdfUrl
    print(pdfFullUrl)
    fileName=secCode+announcementTitle+'.pdf'   #使用证券代码+证券名称命名文件
    pdf_response = requests.get(pdfFullUrl)
    #将请求下来的PDF数据，存储下来
    with open("download_pdf/" + fileName, 'wb') as pdf_file:
        pdf_file.write(pdf_response.content)

