from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'C:\Users\mc_pa\Desktop\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'https://hs3x.com/'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

for tbody in soup.find_all('tbody'):
	

driver.quit()
