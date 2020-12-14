from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'C:\Users\mc_pa\Desktop\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'http://sms-receive.net/'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

div = soup.find('div', class_='uk-grid uk-grid-match uk-grid-width-1-1 uk-grid-width-medium-1-3 tm-grid-height-250')

for a in div.find_all('a'):
	print(a.text)

driver.quit()