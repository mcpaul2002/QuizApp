from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'C:\Users\mc_pa\Desktop\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'http://receivefreesms.com/'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

#for table in soup.find_all('table'):
	#for strong in table.find_all('strong'):
		#print(strong.text)

for table in soup.find_all('table'):
	for a in table.find_all('a'):
		print(a.text)

driver.quit()