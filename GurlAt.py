import requests
import random
import string
import re
import os
from colorama import Fore, init
from urllib.parse import urlparse

init()

cv = Fore.GREEN
cb = Fore.WHITE
caz = Fore.BLUE

def ejecutar_dirb_y_guardar_resultados(url, archivo_salida):
    comando = f"dirb {url} > {archivo_salida}"
    os.system(comando)

def filtrar_directorios_status_200(archivo):
    try:
        with open(archivo, 'r') as file:
            lineas = file.readlines()

        directorios_status_200 = []
        for linea in lineas:
            if re.search(r'\[200\]', linea):
                match = re.search(r'\[200\] (.+)', linea)
                if match:
                    directorio = match.group(1)
                    directorios_status_200.append(directorio.strip())

        return directorios_status_200
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró.")
        return []

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
                
                archivo_resultado = "resultado.txt"
                ejecutar_dirb_y_guardar_resultados(url, archivo_resultado)

                directorios_status_200 = filtrar_directorios_status_200(archivo_resultado)

                # Mostrar los directorios con status 200
                for directorio in directorios_status_200:
                    print(directorio)
                
                with open(archivo, "a") as file:
                    file.write(f"{url}\n")

    except requests.RequestException as e:
        print("Error")

def generador_urls(archivo):
    objetivos = [".gt", ".gob.gt", ".gob", ".gob.ni", ".ni"]
    protocolos = ["http", "https"]
    for _ in range(900000):  # Limitar la cantidad de URLs generadas (puedes ajustar esto)
        protocolo = random.choice(protocolos)
        letras = "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))
        objetivo = random.choice(objetivos)
        url = f"{protocolo}://{letras}{objetivo}"
        verificar_estado_url(url, archivo)

nombre_archivo = "200.txt"
try:
    generador_urls(nombre_archivo)
except KeyboardInterrupt:
    print(f"{Fore.RED}Detenido...")
