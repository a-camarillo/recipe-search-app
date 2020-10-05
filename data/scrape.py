from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('.path.txt','r') as f:
    PATH = f.read()

driver = Chrome(executable_path=PATH)
driver.get('https://tasty.co/topic/5-ingredients-or-less')
