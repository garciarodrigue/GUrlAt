import os
import requests
import random
import string
import re
from colorama import Fore, Back, Style, init
from urllib.parse import urlparse


init()

cv = Fore.GREEN
cb = Fore.WHITE
cn = Fore.BLACK
caz = Fore.BLUE

fr = Back.RED
fm = Back.RESET

def verificar_estado_url(url, archivo):
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(f"{cb}URL{caz} {url}{cv} [+]")
            
            parsed_url = urlparse(url)
            domain_extension = parsed_url.netloc.split('.')[-1]
            if domain_extension == "gt":
                azul = Fore.BLUE
                verde = Fore.GREEN
                print(f"{azul}GT {verde}Encontrado")
                os.system(f"dirb {url} -o {url}.txt")
                
                def filtrar_directorios_status_200(archivo):
                    with open(archivo, 'r') as file:
                        lineas = file.readlines()

                    directorios_status_200 = []
                    for linea in lineas:
                        # Buscar líneas que contengan "Status: 200"
                        if re.search(r'\[200\]', linea):
                            # Extraer el directorio de la línea
                            match = re.search(r'\[200\] (.+)', linea)
                            if match:
                                directorio = match.group(1)
                                directorios_status_200.append(directorio.strip())

                    return directorios_status_200

                archivo_resultado = 'resultado.txt'
                directorios_status_200 = filtrar_directorios_status_200(archivo_resultado)

                # Mostrar los directorios con status 200
                for directorio in directorios_status_200:
                    print(directorio)
                        
                with open(archivo, "a") as file:
                    file.write(f"{url}\n")
                
    except requests.RequestException as e:
       pass

def generador_urls(archivo):
    objetivos = [".gt", ".gob.gt", ".gob", ".gob.ni" ".ni"]
    protocolos = ["http", "https"]
    while True:
        protocolo = random.choice(protocolos)
        letras = "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))

        objetivo = random.choice(objetivos)
        url = f"{protocolo}://{letras}{objetivo}"
            
        verificar_estado_url(url, archivo)

nombre_archivo = "200.txt"
try:
    generador_urls(nombre_archivo)
except KeyboardInterrupt:
    alert = Fore
    print(f"{alert}Detenido...")
