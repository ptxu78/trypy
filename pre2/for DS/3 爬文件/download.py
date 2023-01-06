import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


options = webdriver.ChromeOptions()
options.add_argument('--headless')
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory':"C:\\Users\\pity\\Desktop\\DS_download",#设置默认下载路径
        "profile.default_content_setting_values.automatic_downloads":1}
options.add_experimental_option('prefs', prefs)

browser=webdriver.Chrome(chrome_options=options)

browser.get('http://www.szse.cn/disclosure/listed/notice/index.html')
time.sleep(1)
browser.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/div[1]/div[1]/div/input" ).send_keys("年度股东大会决议")
browser.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div[1]/div[6]/button').click()

startTime = time.time()
page = 1
while page < 51:
    try:
        browser.execute_script("window.scrollBy(0,3000)")
        if page == 1:
            time.sleep(0.3)
            browser.find_element(By.XPATH, '//*[@id="paginator"]/li[19]/a').click()
            page = page + 8
        time.sleep(0.3)
        browser.find_element(By.XPATH, '//*[@id="paginator"]/li[29]/a').click()
        print("skip! page:", page)
        page = page + 1
    except:
        print("page skip error.  page:", page)

while page < 16000:

    browser.execute_script("window.scrollBy(0,3000)")
    time.sleep(0.5)
    pageList = []
    for i in range(1,51):
        # try:
        ucode = browser.find_element(By.XPATH, '//*[@id="disclosure-table"]/div/div[1]/div/table/tbody/tr['+str(i)+']/td[1]/a').text
        uname = browser.find_element(By.XPATH, '//*[@id="disclosure-table"]/div/div[1]/div/table/tbody/tr['+str(i)+']/td[2]/a').text
        utitle = browser.find_element(By.XPATH, '//*[@id="disclosure-table"]/div/div[1]/div/table/tbody/tr['+str(i)+']/td[3]/div/a/span[1]').text
        utime = browser.find_element(By.XPATH, '//*[@id="disclosure-table"]/div/div[1]/div/table/tbody/tr['+str(i)+']/td[4]/span').text
        unitList = [ucode,uname,utitle,utime]
        # 点击下载按钮
        browser.find_element(By.XPATH, '//*[@id="disclosure-table"]/div/div[1]/div/table/tbody/tr[' + str(i) + ']/td[3]//div/a/span[3]').click()

        pageList.append(unitList)
        # except:
        #     print("unit:", i, "error. page:", page)

    df = pd.DataFrame(pageList)
    df.to_csv("1.csv", header=False, index=False, mode='a')

    browser.find_element(By.XPATH, '//*[@id="paginator"]/li[29]/a').click()

    time.sleep(1)
    print("page finish.  page:", page," timeUsed: ", time.time()-startTime)

    page = page + 1

