from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'C:\Users\mc_pa\Desktop\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'https://www.receivesmsonline.net/'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

div = soup.find('div', class_='row')

for h2 in div.find_all('h2'):
	print(h2.text)

driver.quit()

