from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests
from selenium import webdriver

my_url = 'https://sg.carousell.com/search/ipad%20pro?condition_v2=USED&sc=1202081422120a0c74696d655f63726561746564120208002a160a0c636f6e646974696f6e5f763222060a04555345442a160a0c636f6e646974696f6e5f763222060a0455534544320a0a08697061642070726f3a0408bbe17242037765624a02656e&sort_by=time_created%2Cdescending'
driver = webdriver.Chrome()
driver.get(my_url)


page_soup = soup(driver.page_source,'html.parser')
containers = page_soup.findAll('div', {'class':'An6bc8d5sQ _9IlksbU0Mo _2t71A7rHgH'})

for i,container in enumerate(containers):
        desc = container.div.findAll('a')
        try:
                desc_time = desc[0].findAll('div')
                desc_time = desc_time[len(desc_time)-1].text
        except:
                desc_time = 'New Carousell'
        desc_obj = desc[1].findAll('p')
        print('\nitem:', i+1)
        print('posted :',desc_time)
        print(len(desc_obj))

