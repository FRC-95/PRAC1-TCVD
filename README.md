## PRAC1-TCVD
# Tipología y ciclo de vida de los datos : Web Scraping

El objetivo de esta practica es familiarizarse con la herramientas de Python para Web Scraping.

Para replicar los resultados aqui mostrados, resulta imprescindible el uso de la libreria BeautifulSoup, instalable mediante el gestor de paquetes pip con el comando `pip install beautifulsoup4` e importado posteriormente mediante `from bs4 import BeautifulSoup`.

El script de scraping cuenta con dos funciones: scraping de datos de clasificación de liga y scraping de resultados de partidos.



### Set de datos

El set de datos mostrado en el csv es el referente a scraping de resultados. El formato resultante es tal que:

| fecha  | campo | jornada | local | local_goles | visitante_goles | visitante | 
| ---------- | ---------- | ---------- | ---------- | ---------- |---------- |---------- |
| 21.10.2018 | CIU UCM - UCM 1 | 1 | CONTINOX CAVANNA | 14 | 0 | RAYAS BLANCAS |
| 21.10.2018 | CIU UCM | 1 | 43 | GOLAZOS | 0 | 7 | SEKTA |

Donde cada atributo viene definido por:

* *fecha*: la fecha en la que se disputó o se disputará el aprtido
* *campo*: el campo donde se disputa el partido
* *jornada*: la jornada a la que corresponde ese partido
* *local*: nombre del equipo local
* *local_goles*: número de goles del equipo local
* *visitante_goles*: número de goles del equipo visitante
* *visitante*: nombre del equipo visitante
