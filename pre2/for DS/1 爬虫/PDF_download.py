import openpyxl
import requests

wb = openpyxl.load_workbook('C:/Users/79942/Desktop/宝贝的中小股东公司治理参与度指标/2014-2020深市中小股东股东大会决议公告下载链接.xlsx')  # 输入存放url链接的Excel电脑路径，可以修改
sheet = wb['Sheet1']  # excel的sheet页，可以修改

for i in range(19990,32545):  # excel中数据的行数，我这里是30条，可以修改
    try:

        name = sheet['A' + str(i + 1)].value  ##此为PDF的命名，名字在表中A列
        url = sheet['B' + str(i + 1)].value  ##PDF链接在表中B列，根据实际情况做更改
        pdf = open('C:/Users/79942/Desktop/宝贝的中小股东公司治理参与度指标/1/' +str(i)+'-'+ str(name) + '.pdf', 'wb')
        print(i)
        res = requests.get(url)
        pdf.write(res.content)
        #for chunk in res.iter_content(100000):
            #pdf.write(chunk)
        pdf.close()
    except:
        print('error ',i)