''' 
Como podemos identificar los elementos?
Id
Name
Link Text
Partial Link Test
Xpath
CSS Selector
Tag Name
Class

Id
Es el selector mas directo que hay. Usarlo siempre que sea posible.
Ventaja: es único, no hay chance de confundirse con otro elemento.
Desventaja: Si el sitio usa Id dinámico, no puedo usarlo.
'''
<input type="text" id="myText" size="30">

inputText = driver.find_element_by_id('myText')


'''
Name
Selecciona por nombre identificadorio del tag. Similar al Id.
Ventaja: Es altamente probable que el name no esté repetido.
Desventaja: Puede repetirse.
'''
<input type="name" id="userName" size="30">

inputText = driver.find_element_by_name('userName')


'''
Link Text
Seleccionar por el texto de un link
Ventaja: Sencillo de usar, solo hay q reconocer el texto del link.
Desventaja: se puee repetir en varios lugares.
'''
<a href="mienlace.html">ir a mi enlace</a>

inputText = driver.find_element_by_link_text('ir a mi enlace')


'''
Partial Link Text
Seleccina por una parte del texto de un link
Ventaja: Si no conocemos TODO el texto del link en un momento podemos usarlo
(situaciones en las que el link se arma de acuerdo a datos)
Desventaja: Repeticion
'''
<a href="mienlace.html?v=1234">ir al cliente 1234</a>

inputText = driver.find_element_by_partial_link_text('ir al cliente')


'''
Xpath
Navegacion a traves de los elementos
Ventaja: si no tenemos otros selectores disponiles, un Xpath bien armado es una 
buena solucion
Desventaja: Un Xpath mal armado nos puede traer problemas de repetición o de movimiento
del elemento

el // es como un posicionamiento relativo
Selenium convierte el id en un Xpath y se lo pasa al webdriver, y este lo trabaja como
si le hubiese pasado un Xpath
'''
<input type="text" size="30">

inputText = driver.find_element_by_xpath('/html/body/form/input[1]')
inputText = driver.find_element_by_xpath('//form/input[1]')


'''
CSS Selector
Ventaja: Si no tenemos otros selectores disponibles, un CSS bien armado es 
una buena solución
Desventaja: Puede haber multitud de elementos con el mismo selector CSS
'''
<p class="paragraphModel">

inputText = driver.find_element_by_css_selector('p.paragraphModel')


'''
Tag Name
Buscar por etiqueta
Ventaja: en la practica solo se usa en momentos en los que deliberadamente
queremos algo que se repite mucho
Desventaja. Dificilmente pueda ser usado para buscaar elementos unicos.
'''
<h3>Subtitle</h3>

inputText =  driver.find_element_by_tag_name('h3')


'''
Class Name
Busca por la clase
ventaja: solo lo vamos a usar cuando queramos duplicados o sepamos que 
esa clase solo es usda sobre una etiqueta unicamente
Deventaja: Dificilmente pueda ser usada para buscar eleementos unicos
'''
<p class="paragraphModel">

inputText = driver.find_element_by_class_name('p.paragraphModel')
