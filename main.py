import concurrent.futures
import requests
import json


DEBUG = True
URL = 'https://api.sioma.dev/4/testing/mover_coordenadas/'
NPROC = 100
OUT = []
JSONFILE = "data.json"
if DEBUG:
    JSONFILE = "prueba.json"


def Get_urls(jsonFile, debug=False):
    """Funcion que importa un archivo json y devuelve un array con las urls"""
    with open(jsonFile) as f:
        data = json.load(f)
    urls = []
    for i in data:
        # Combinar la url con las fechas y la finca_id
        url = URL + str(i['fechaInicial']) + '/' + str(i['fechaFinal']) + '/' + str(i['finca_id'])
        urls.append(url)
    return urls


def Web_conex(url, timeout=300, save_html_file=False):
    array = []
    header = {"Authorization": "fUeIDNc5YscqxJqjTn+SesYXYgoYI35OaC74k3l5KOM=",
              "julio": "h01oeai/xaIV9FGoWjY3PgNyHNwTsZU/u0RXB6Sbt9Y="}
    print(url)
    page = requests.get(url, headers=header, timeout=timeout)
    if save_html_file:
        with open('response.html', 'w') as f:
            f.write(str(page.content).strip('\n'))
    return str(page.content)


if __name__ == '__main__':
    # Obtener las urls
    urls = Get_urls(JSONFILE, DEBUG)
    Web_conex(urls[0], save_html_file=True)

    # Crear la concurrencia
    # with concurrent.futures.ThreadPoolExecutor(max_workers=NPROC) as executor:
    #     # Ejecutar las peticiones
    #     results = (executor.submit(Web_conex, url) for url in urls)
    #     for f in concurrent.futures.as_completed(results):
    #         try:
    #             data = f.result()
    #         except Exception as exc:
    #             data = str(type(exc))
    #         finally:
    #             OUT.append(data)
    #             print(str(len(OUT)), end='\r')
    # print(OUT)
