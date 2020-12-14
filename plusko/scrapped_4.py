from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'C:\Users\mc_pa\Desktop\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'http://freesmsverification.com/'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

for tr in soup.find_all('tr'):
	for a in tr.find_all('a'):
		print(a.text)

driver.quit()