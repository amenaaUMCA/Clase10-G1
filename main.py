# Proyecto: [Clase 10 - Fundamentos de Python]
# Estudiante: [Prof. Andrés Mena]
# Fecha de Inicio: [2025/03/26]
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.
 
#from analisis_datos.carga_datos import generar_lista_compras
#from analisis_datos.estadisticas import media, mediana

from analisis_datos import *

lista_compras = generar_lista_compras()
print(lista_compras)

precios = [valor for producto,valor in lista_compras]

print('La media arimetica de la compra es :', media(precios))
print('La mediana de la compra es : ', mediana(precios))
