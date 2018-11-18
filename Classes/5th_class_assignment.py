
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/yarzi01/Documents/DevOps/chromedriver")
driver.get("https://google.co.il/")

# driver = webdriver.Firefox(executable_path="/Users/yarzi01/Documents/DevOps/geckodriver")
# driver.get("https://google.co.il/")
# driver.get("https://ynet.co.il/")

element = driver.title
driver.refresh()
if element == driver.name:
    print("name is the same")
else:
    print("name is different")




