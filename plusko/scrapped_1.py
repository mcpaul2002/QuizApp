from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'C:\Users\mc_pa\Desktop\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url='http://receive-sms-online.com/'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

div = soup.find('div', id='content')

for a in div.find_all('a'):
	print(a.text)

driver.quit()