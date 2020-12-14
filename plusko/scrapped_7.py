from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'C:\Users\mc_pa\Desktop\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'https://www.receiveasms.com/'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

article = soup.find('article', class_='item item-page')

for b in article.find_all('b'):
	print(b.text)

driver.quit()
