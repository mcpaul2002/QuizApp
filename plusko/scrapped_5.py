from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'C:\Users\mc_pa\Desktop\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'https://www.freeonlinephone.org/'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

div = soup.find('div', class_='newsletter color-1')

for h4 in div.find_all('h4'):
	print(h4.text)

driver.quit()