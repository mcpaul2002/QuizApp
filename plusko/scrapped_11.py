from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'C:\Users\mc_pa\Desktop\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'http://sms.sellaite.com/'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

for td in soup.find_all('td'):
	for h1 in td.find_all('h1'):
		print(h1.text)

driver.quit()

