import pywifi
from pywifi import *
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

username = input('请输入你的学号：\n')
password = input('请输入你的校园网密码：\n')
wifiname = input('请输入你要链接的校园WiFi名称：\n')
wifipsw = input('请输入你要连接的校园WiFi的密码（没有则直接enter）：\n')

profile=pywifi.Profile()
profile.ssid=wifiname
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = wifipsw

wifi=pywifi.PyWiFi()
iface = wifi.interfaces()[0]
profile = iface.add_network_profile(profile)
iface.connect(profile)

time.sleep(5)
if iface.status()==const.IFACE_CONNECTED:
    print('connect successful!')
else:
    print('connect failed!')





browser = webdriver.Chrome()


url = 'https://u.njtech.edu.cn/cas/login?service=https%3A%2F%2Fu.njtech.edu.cn%2Foauth2%2Fauthorize%3Fclient_id%3DOe7wtp9CAMW0FVygUasZ%26response_type%3Dcode%26state%3Dnjtech%26s%3Df682b396da8eb53db80bb072f5745232'


browser.get(url)





username = browser.find_element_by_name('username')
username.send_keys(username)


password = browser.find_element_by_name('password')
password.send_keys(password)


student = browser.find_element_by_name('channelshow')
student.click()


cmcc=browser.find_element_by_xpath('//span[@value="@cmcc"]')
cmcc.click()


login_button = browser.find_element_by_name('login')
login_button.submit()


browser.save_screenshot('picture1.png')

text=browser.page_source.encode('utf-8').decode()
soup=bs(text,'html.parser')
try:
    q=soup.find('div',class_='g-ngd-top-1')
    print('{}'.format(q.text))
except:
    print('登陆失败')

browser.quit()
