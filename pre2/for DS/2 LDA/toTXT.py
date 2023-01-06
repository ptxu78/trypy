import pandas as pd

df = pd.read_excel('1.xlsx', header=None)		# 使用pandas模块读取数据
# print(df[7])
for i in range(len(df)):
    a = df.loc[i]
    f = open('./txt/'+str(i)+'.txt', 'w', encoding='utf-8')
    f.write(a[7])
    f.close()
