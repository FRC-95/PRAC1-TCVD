from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import csv

# Funcion para obtener datos de la web
## Se pasa como parametros el sitio web y la pagina enc oncreto
def scrapDatos( website, page ):
    url = website + page
    content = urlopen(url).read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup


# Funcion para obtener datos acerca de la clasificación
def scrapClasificacion( soup ):

    # Se busca la tabla
    table = soup.find('table')

    # Se crea una variable auxiliar para eliminar el indice 0
    first = 0

    # Se buscan en la tabla los diferentes datos
    for row in table.findAll("tr"):
        cells = row.findAll('td')
        if(first > 0):
            # index 0 of cells doesn't have info
            POS = int(cells[1].find(text=True).replace('.', ''))
            PTS = int(cells[4].find(text=True))
            J   = int(cells[5].find(text=True))
            G   = int(cells[6].find(text=True))
            E   = int(cells[7].find(text=True))
            P   = int(cells[8].find(text=True))
            GF  = int(cells[9].find(text=True))
            GC  = int(cells[10].find(text=True))
            DG  = int(cells[11].find(text=True).replace('\xa0', ''))

            obs = [POS, PTS, J, G, E, P, GF, GC, DG]
            obsList.append(obs)
        first = first + 1

# Funcion para obtener datos acerca de los partidos
def scrapResultados( soup ):

    # Se busca la tabla
    table = soup.find('table')

    # Se crea una variable auxiliar para eliminar el indice 0
    first = 0

    # Se crea una variable auxiliar para el numero de jornada
    # Este numero es comun para varias filas (varios partidos)
    jornada = 0
    for row in table.findAll('tr'):
        cells = row.findAll('td')
        if(first > 0):
            # Si cambia la jornada, se suma uno a su valor
            if(str(cells).find('Jornada') == 56):
                jornada = jornada + 1
            else:
                fecha_campo = cells[1].text.split()
                fecha = fecha_campo[0]
                campo = ' '.join(fecha_campo[1:len(fecha_campo)])
                local = cells[2].text.strip()
                resultado = cells[3].text.replace('-',' ').split()
                # Si el resultado no tiene dos valores, es un partido sin jugar
                if(len(resultado) == 1):
                    lGoles = 'N/D'
                    vGoles = 'N/D'
                else: 
                    lGoles = resultado[0]
                    vGoles = resultado[1]
                visitante = cells[4].text.strip()

                partido = [fecha, campo, jornada, local, lGoles, vGoles, visitante]
                lista_partidos.append(partido)

        first = first + 1

# El sitio web del que obtener los datos
website = 'http://www.torneosfutbolsiete.com'

# Subdominio para la clasificacion
page = '/futbol-7-madrid-fin-de-semana-2018/clasificacion'
soup = scrapDatos( website, page)

# Lista para guardar datos de clasificacion
obsList = ['POS', 'PTS', 'J', 'G', 'E', 'P', ' GF', 'GC', 'DG']
scrapClasificacion(soup)

# Subdominio para los resultados
page = '/futbol-7-madrid-fin-de-semana-2018/resultados'
soup = scrapDatos( website, page)

# Lista para guardar datos de resultados
lista_partidos = ['fecha', 'campo', 'jornada', 'local', 'local_goles', 'visitante_goles', 'visitante']
scrapResultados(soup)

# Se define el path para guardar el dataset
path = os.path.dirname(__file__)
nombre = "resultados_futbol.csv"
path = os.path.join(path, nombre)

# Se guardan los datos del dataset
with open(path, 'w', newline = '') as csvFile:
  writer = csv.writer(csvFile)
  # En primer lugar las cabeceras de los atributos
  writer.writerow(lista_partidos[0:7])
  del lista_partidos[0:7]
  # Y a continuacion los datos
  for partido in lista_partidos:
    writer.writerow(partido)

