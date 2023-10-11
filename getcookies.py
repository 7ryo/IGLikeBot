import json
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get('https://www.instagram.com/')

time.sleep(20)

## save cookies as json
with open('cookies.json','w') as f:
    f.write(json.dumps(driver.get_cookies()))


driver.close()
