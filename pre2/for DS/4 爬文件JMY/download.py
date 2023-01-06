import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory':"C:\\Users\\xuhaoran\\Desktop\\download-forum",
        "profile.default_content_setting_values.automatic_downloads":1}
options.add_experimental_option('prefs', prefs)
browser=webdriver.Chrome(chrome_options=options)
action = ActionChains(browser)
browser.get('https://forum-portal.thirdbridge.com/')
time.sleep(3)

# login
userNameList = ["wb@sourcecodecap.com", 'ldq@sourcecodecap.com']
pwdList = ["Dahaiwuliang!2", 'Ldq888...']
useMember = 1

browser.find_element(By.XPATH, '//*[@id="userName"]' ).send_keys(userNameList[useMember])
browser.find_element(By.XPATH, '//*[@id="userPassword"]' ).send_keys(pwdList[useMember])
browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/form/div[5]/button').click()
time.sleep(5)

# clear ad
browser.find_element(By.XPATH, "/html/body/div[1]/div/a[1]").click()
time.sleep(0.5)


# change to 100/page
browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div[3]/div/div[2]/div[1]/div[2]').click()
time.sleep(2)

browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]').click()
time.sleep(3)

startTime = time.time()
page = 1

# skip page
# while page < 5:
#     try:
#         # browser.execute_script("window.scrollBy(0,3000)")
#         time.sleep(3)
#         # if page == 1:
#         #     browser.find_element(By.XPATH, '//*[@id="paginator"]/li[19]/a').click()
#         #     page = page + 8
#         browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div[4]/ul/li[3]/a').click()
#         print("skip! page:", page)
#         page = page + 1
#     except:
#         print("page skip error.  page:", page)

while page < 400:

    # browser.execute_script("window.scrollBy(0,3000)")
    # pageList = []
    for i in range(1,101):
        try:
            # 点击下载按钮
            browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div/div[2]/div[2]/table/tbody/tr[' + str(i) + ']/td[2]/div[3]/button[3]/div/img').click()
            time.sleep(0.5)
            browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/div/span/div').click()
            time.sleep(0.5)
            action.move_by_offset(0, 0).click().perform()
            time.sleep(0.5)
            print("unit:", i, " download success. page:", page)

            # pageList.append(unitList)
        except:
            print("\tunit:", i, " can not download. page:", page)

    # df = pd.DataFrame(pageList)
    # df.to_csv("1.csv", header=False, index=False, mode='a')
    time.sleep(1)
    action.move_by_offset(0, 0).click().perform()
    browser.execute_script("window.scrollBy(0,-3000)")
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div[4]/ul/li[3]/a').click()


    print("page finish.  page:", page," timeUsed: ", time.time()-startTime)
    time.sleep(8)
    page = page + 1

