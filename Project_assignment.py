# coding=utf-8

import time                     #allow using sleep commands


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="/Users/yarzi01/Documents/DevOps/chromedriver")
driver.get("https://buyme.co.il/")              #open the webpage
driver.fullscreen_window()
time.sleep(5)

#account registration section
# button_element = driver.find_element_by_class_name("seperator-link")        #finding the  registration button
# button_element.click()                                                      #and click it
#
# time.sleep(2)
# driver.find_element_by_class_name("text-btn").click()                       #finding הרשמה
# driver.find_element_by_id("ember973").click()                               #and click it
# time.sleep(2)
# driver.find_element_by_id("ember973").send_keys('Ziv')                      #sending the first name to the correct field
#
# driver.find_element_by_xpath("//input[@placeholder='מייל']").send_keys("zz@kalamazoo.com")  #sending email address
# driver.find_element_by_xpath("//input[@placeholder='סיסמה']").send_keys("aB123456")         #sending password
# driver.find_element_by_xpath("//input[@placeholder='אימות סיסמה']").send_keys("aB123456")   #password verification
# driver.find_element_by_class_name("fa-check ").click()                                      #click the checkbox
#
# driver.find_element_by_css_selector("#ember971 > button").click()                           #clicking button נרשמה
# time.sleep(2)

#website login section after registration
driver.find_element_by_css_selector("#ember577 > div > ul.nav-bar.buttons > li:nth-child(3)").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@placeholder='מייל']").send_keys("zz@kalamazoo.com")  #sending email address
driver.find_element_by_xpath("//input[@placeholder='סיסמה']").send_keys("aB123456")
driver.find_element_by_xpath("//input[@placeholder='סיסמה']").send_keys("\n")   #sending password
time.sleep(1)
#open the dropdown list and choose 4th option
driver.find_element_by_css_selector("#ember650_chosen").click()
driver.find_element_by_css_selector("#ember650_chosen > div > ul > li:nth-child(4)").click()
time.sleep(1)
#open the dropdown list and choose 2nd option
driver.find_element_by_css_selector("#ember665_chosen").click()
driver.find_element_by_css_selector("#ember665_chosen > div > ul > li:nth-child(2)").click()
time.sleep(1)
#open the dropdown list and choose 4th option
driver.find_element_by_css_selector("#ember674_chosen").click()
driver.find_element_by_css_selector("#ember674_chosen > div > ul > li:nth-child(4)").click()
time.sleep(1)
#click the חפש לי מתנה button
driver.find_element_by_xpath("//form/a").click()
time.sleep(2)

#choosing category from the listed options
driver.find_elements_by_tag_name("label").__getattribute__("label:Loveat לאבאיט")






# button_element = driver.find_elements_by_class_name("seperator-link")

# button_element = driver.find_elements_by_xpath('//input[@type = )
# button_element.click()

# element = driver.find_element(by.ID,value="ember577")

# element = driver.find_element_by_id("gt-submit")
# element = driver.find_elements_by_class_name("jfk-button")

# driver.find_element_by_link_text("Click Now")           #find by full test
# driver.find_element_by_partial_link_text('ember577')      #find by pasrtial test

# driver.find_element_by_xpath('//input[@type = 'Submit']')
# driver.find_element_by_xpath('//input[@type = 'Submit' and @tabindex = '0']')

# Xpath helper for Chrome will show the full path to the element we point with the mouse and cab be
# easily used as the value for the absulute Xpath
# Xpath should NOT be the default for searching element, but only if there is no other option

# driver.find_element_by_id("firstButton").click()
# #another option is to create object:
# button_element = driver.find_element_by_id("myButton")
# button_element.click()

# calling submit function will bypass the screen button
# sendKeys is sending the test to the element we are looking for
# first we find the element by ID then we send the text back to the same element

# driver.find_element_by_id("source").send_keys("good morning")
# driver.implicitly_wait(5)
# x = driver.find_element_by_id("gt-tl-gms")
# x.click()
# my_langList = driver.find_elements(By.ID, value = "gt-tl-gms")


# driver.find_element_by_Xpath('//div[@aria-activedescendant = ':3y']')
# driver.find_element_by_xpath('//input[@type = 'Submit']')


# print(driver.page_source)
# driver.back() / .forward() /

# driver.close()


# driver.quit()
