import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/yarzi01/Documents/DevOps/chromedriver")
driver.get("https://translate.google.com/")

driver = webdriver.Firefox(executable_path="/Users/yarzi01/Documents/DevOps/geckodriver")
driver.get("https://ynet.co.il/")

# time.sleep(5)
print(driver.current_url)
print(driver.title)
# element = driver.find_element(by.ID,value="gt-submit")
element = driver.find_element_by_id("gt-submit")
element = driver.find_elements_by_class_name("jfk-button")

# driver.find_element_by_link_text("Click Now")           #find by full test
# driver.find_element_by_partial_link_text('Click"')      #find by pasrtial test

#driver.find_element_by_xpath('//input[@type = 'Submit']')
#driver.find_element_by_xpath('//input[@type = 'Submit' and @tabindex = '0']')

# Xpath helper for Chrome will show the full path to the element we point with the mouse and cab be
# easily used as the value for the absulute Xpath
# Xpath should NOT be the default for searching element, but only if there is no other option

# driver.find_element_by_id("firstButton").click()
# #another option is to create object:
# button_element = driver.find_element_by_id("myButton")
# button_element.click()

#calling submit function will bypass the screen button
#sendKeys is sending the test to the element we are looking for
#first we find the element by ID then we send the text back to the same element

driver.find_element_by_id("source").send_keys("good morning")
driver.implicitly_wait(5)
x = driver.find_element_by_id("gt-tl-gms")
x.click()
my_langList = driver.find_elements(By.ID, value = "gt-tl-gms")



# driver.find_element_by_Xpath('//div[@aria-activedescendant = ':3y']')
# driver.find_element_by_xpath('//input[@type = 'Submit']')








# print(driver.page_source)
# driver.back() / .forward() /

#driver.close()



#driver.quit()
