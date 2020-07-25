from selenium import webdriver

#necesito esto para la prueba, si no solo seria una navegacion
import unittest
import time

# Mal, pero para practicar al no saber POO. Inicializo el test case
tc = unittest.TestCase('__init__')

# selenium no interactua con el browser, necesito un webdriver para eso.
# cada browser tiene el suyo, ejemplo chromedriver
driver = webdriver.Chrome("chromedriver.exe")

#pongo a donde tengo que navegar, usamos automationpractice.com
# mi caso de prueba va ser buscar "hola" y el resultado tiene que ser "No results were found for your search "hola""
driver.get('http://automationpractice.com/index.php')

# ahora si ejectuto desde la consola test.py, se abre el browser con la web

# ahora quiero escribir en la barra de busqueda. tomo un elemento e interactuo con el mismo
driver.find_element_by_id("search_query_top").send_keys("hola")
driver.find_element_by_name("submit_search").click()

# hacemos click derecho sobre el resultado desde el inspector para copiar el xpath y va ser lo q se comparar con lo deseado
#driver.find_element_by_xpath('//*[@id="center_column"]/p')

time.sleep(10)

# verificacion
tc.assertEqual('No results were found for your search "hola"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text)


driver.close()
driver.quit()

# lo probamos desde la consola. puede que no haya encontrado el elemento, pq fue a buscar el elemento antes de que termine
# de cargar la pagina
#con time.sleep(), detengo la ejecucion hasta que cargue la pagina

