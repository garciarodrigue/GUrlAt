import os
import requests
import random
import string
from colorama import Fore, Back, Style, init
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
            print(f"{cb}URL{caz} {url}{cv} [+]");
            
            with open(archivo, "a") as file:
                file.write(f"{url}\n")
                if url == ".gt":
                    print("gt encontrado")
                
    except requests.RequestException as e:
        pass
def generador_urls(archivo):
    objetivos = [".gt", ".com", ".gob", ".nc"]
    protocolos = ["http", "https"]
    while True:
        protocolos = random.choice(protocolos)
        letras = "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))

        objetivos = random.choice(objetivos)
        cr = Fore.RED
        url = f"{protocolos}://{letras}{objetivos}"
            
        verificar_estado_url(url, archivo)
            
nombre_archivo = "200.txt"
try:
    generador_urls(nombre_archivo)
except KeyboardInterrupt:
                    
        alert = Fore
        print(f"{alert}detenico...")
            