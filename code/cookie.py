from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl

# 创建 Chrome webdriver 对象
driver = webdriver.Chrome()

# 访问qunar登录页面
driver.get("https://hotel.qunar.com/")

# 填写表单，模拟登录豆瓣
log = driver.find_element(By.XPATH, '//*[@id="__headerInfo_login__"]')
log.click()
choice = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]')
choice.click()
username = driver.find_element(By.XPATH, '//*[@id="username"]')
password = driver.find_element(By.XPATH, '//*[@id="password"]')
confirm = driver.find_element(By.XPATH, '//*[@id="agreement"]')
submit_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div/div[3]')

username.send_keys("yourID")
password.send_keys("yourPassword")
confirm.click()
submit_btn.click()

# 等待登录成功后，获取当前页面的 cookies
driver.implicitly_wait(10)
cookies = driver.get_cookies()
print(cookies)

# 关闭 webdriver
driver.quit()

# 创建一个新 webdriver
driver2 = webdriver.Chrome()

# 打开需要访问的页面
driver2.get("https://hotel.qunar.com/")
# 添加 cookies 到 webdriver
for cookie in cookies:
    driver2.add_cookie(cookie)

# 刷新页面，此时就能够免登录访问了
driver2.refresh()
time.sleep(10)