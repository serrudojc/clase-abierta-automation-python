from selenium import webdriver

import unittest
import time


tc = unittest.TestCase('__init__')

driver = webdriver.Chrome("chromedriver.exe")
driver.get('http://automationpractice.com/index.php')

#driver.find_element_by_id("search_query_top").send_keys("hola")
#driver.find_element_by_name("submit_search").click()
# NUNCA DEJAR CODIGO COMENTADO (esto es una practica)

# cuando quiero interactuar con un elemento, tengo q agarrar al elemento y trabajar con él
# PREGUNTA DE ENTREVISTA: de que forma puedo encontrar elementos? por id, name, xpath, etc (tratar de evitar el xpath pq puede cambiar)
seach_box = driver.find_element_by_id("search_query_top")
seach_box.send_keys("hola mundo")

seach_box_button = driver.find_element_by_name("submit_search")
seach_box_button.click()

time.sleep(5)

#tc.assertEqual('No results were found for your search "hola mundo"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text)

# el unittest es el que se encarga de armar los asserts, este caso pasó o no. No lo hace selenium
# Nosotros creamos un elemento tc
# assertEqual comparara dos cosas y devuelve un Booleano.
# Primer parámetro es nuestro texto resultado esperado
# Segundo parametro, contra que lo queremos comparar, extraemos el texto. Inspeccionamos en el html pero
# no tenemos id o name, usamos xpath entonces.
# El xpath recorre el html hasta un punto, html/body/form/label...
# pero si muevo el elemento de lugar, entonces el xpath ya no sirve.

#usamos el copy Full xpath (absoluto) o el relativo:
results_label = driver.find_element_by_xpath('//*[@id="center_column"]/p')
tc.assertEqual('No results were found for your search "hola mundo"',results_label.text)

# women_link = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[1]/a')
women_link = driver.find_element_by_link_text("Women")
women_link.click()
time.sleep(5)

#supongamos que no tengo o no conozco todo el linktext
dress_link = driver.find_element_by_partial_link_text("Dres")
dress_link.click()
time.sleep(5)


driver.close()  # cierra el browser
driver.quit()   # cerrar sesion del webdriver, usa una API


