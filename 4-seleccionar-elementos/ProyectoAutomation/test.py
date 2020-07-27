from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')

driver = webdriver.Chrome("chromedriver.exe")
driver.get('http://automationpractice.com/index.php')

driver.find_element_by_id("search_query_top").send_keys("hola mundo")

driver.find_element_by_name("submit_search").click()
time.sleep(2)

tc.assertEqual('No results were found for your search "hola mundo"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text)

women_link = driver.find_element_by_link_text("Women").click()
time.sleep(2)

dress_link = driver.find_element_by_partial_link_text("res").click()
time.sleep(2)

# Busco por Link Text
driver.find_elements_by_link_text('Casual Dresses').click()

#Busco por Partial Link Text
driver.find_elements_by_partial_link_text('Casual').click()

# Entro por class name
driver.find_elements_by_class_name('subcategory-name').click()

# Busco cpor css selector
driver.find_elements_by_css_selector('a.subcategory-name').click()

# Busco por Xpath
driver.find_elements_by_xpath('//*[@id="subcategories"]/ul/li[1]/h5/a').click()

#Busco por tag (pero tengo muchos links a)
driver.find_elements_by_tag_name('a').click()

driver.close()  
driver.quit()   