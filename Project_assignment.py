# coding=utf-8

import time
#allow using sleep commands


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#variables declaration
BEIT_ESEK = "בנדיקט"

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
#####################this is the end of the first time registration and then I have replaced it with login process######

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
time.sleep(3)

#scrolling the window
driver.execute_script("window.scrollTo(0, 500)")

#choosing business from the listed option
driver.find_element_by_partial_link_text("בנדיקט").click()
time.sleep(2)
#entering price
driver.find_element_by_css_selector("#ember1168").send_keys("200\n")
time.sleep(1)
#click to someone
driver.find_element_by_xpath("//*[@id='ember1239']/label[1]").click()
time.sleep(1)

#entering the "to" field
driver.find_element_by_xpath("//*[contains(@data-parsley-required-message,'מי הזוכה המאושר')]").click()
driver.find_element_by_xpath("//*[contains(@data-parsley-required-message,'מי הזוכה המאושר')]").clear()
#entering the name
driver.find_element_by_xpath("//*[contains(@data-parsley-required-message,'מי הזוכה המאושר')]").send_keys("Yury")
time.sleep(1)
#from field
driver.find_element_by_xpath("//*[contains(@data-parsley-required-message,'למי יגידו תודה')]").click()
#clear the field
driver.find_element_by_xpath("//*[contains(@data-parsley-required-message,'למי יגידו תודה')]").clear()
#from name
driver.find_element_by_xpath("//*[contains(@data-parsley-required-message,'למי יגידו תודה')]").send_keys("Anonymous")

#choosing event from list
driver.find_element_by_xpath("//a/span[contains(text(), 'לאיזה אירוע')]").click()
driver.find_element_by_xpath("//ul/li[contains(text(), 'יום נישואין')]").click()
#greeting
driver.find_element_by_xpath("//*[contains(@placeholder,'מזל טוב')]").click()
driver.find_element_by_xpath("//*[contains(@placeholder,'מזל טוב')]").clear()
driver.find_element_by_xpath("//*[contains(@placeholder,'מזל טוב')]").send_keys("All the BEST")

#uploading picture - CURRENTLY THIS IS THE ONLY ACTION WHICH DOESNT WORK SINCE IT IS NOT LIKE IN WINDOWS
# WHERE YOU CAN SEND THE FILE PATH
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# driver.execute_script("window.scrollTo(0, 500)")
#time.sleep(1)
# driver.find_element_by_class_name("ui-file").click()
# driver.find_element_by_class_name("ui-file").send_keys("image001.png\n")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#choosing payment
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(1)
driver.find_element_by_class_name('send-now').click()
driver.find_element_by_class_name("btn-send-option-inner").click()
#clear field and send the phone number
driver.find_element_by_xpath("//*[contains(@placeholder,'ספרות בלבד')]").clear()
driver.find_element_by_xpath("//*[contains(@placeholder,'ספרות בלבד')]").send_keys("0526626669")
#clear field and send the phone number
driver.find_element_by_xpath("//*[@id='resendReciver']").clear()
driver.find_element_by_xpath("//*[@id='resendReciver']").send_keys("0526655664")
#click the save button
driver.find_element_by_xpath("//*[@id='ember1232']/div[4]/div/div[4]/div[2]/button[2]").click()
#scrolling down and click the final payment buttin
driver.execute_script("window.scrollTo(0, 300)")
time.sleep(1)
driver.find_element_by_xpath("//button[text()='תשלום']").click()

driver.close()

#driver.quit() - I left it in remark so I can record the screen
#end of project file
#blablalblablblabalbalbalbalbalblbalbalbalbalbalb
g