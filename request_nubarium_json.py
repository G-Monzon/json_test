"""
Pendiente autenticación con Basic Auth y el webhook que obtendrá los datos.
Ver cómo es que Nubarium devuelve el JSON y ver si se tiene que convertir o extraer.
Colocar el webhook en su lugar en la función de payload_mes_nubarium como default.
Colocar en las variables globales el usuario y password de Nubarium.

Nota: Podría ser que la autenticación básica se tenga que colocar en el header con
la llave "Authorization" y como valor:

    Basic user:password

La parte "user:password" es en base64.
"""
# Este import es solo para hacer pruebas, el string real debe llegar a este módulo
from crear_lista_conceptos_de_un_mes import json_string_prueba

import requests
from requests.auth import HTTPBasicAuth

# De preferencia, establecer estas variables como Variables de Entorno
user = 'nubarium'
passw = '_nub4r1mp4ssw0rd.'
basic = HTTPBasicAuth(user, passw)


def solicitar_facturacion_mes(rfc, password, mes, anio):
    payload = payload_mes_nubarium(rfc, password, mes, anio)
    response = request_nubarium_json(payload)
    # return response.json()
    return json_string_prueba


def payload_mes_nubarium(p_rfc, p_password, p_mes, p_anio,
                         p_ordenar_por='monto',
                         p_incluir_xml='true',
                         p_url_nuestro_webhook='https://ejemplo.com/webhook/test'):
    payload_creado = f"""{{
    "rfc": "{p_rfc}",
    "password": "{p_password}",
    "mes": {int(p_mes)},
    "anio": {int(p_anio)},
    "ordenarPor": "{p_ordenar_por}",
    "incluirXML" : {p_incluir_xml},
    "url": "{p_url_nuestro_webhook}"\n}}"""
    return payload_creado


def request_nubarium_json(datos, header=None, url="https://isat.nubarium.com/sat/v1/get-invoices"):
    if header is None:
        header = {}
    response = requests.request("POST", url, headers=header, data=datos, auth=basic)
    # print(response.json())
    return response.json()


if __name__ == '__main__':
    payl = payload_mes_nubarium('Prueba', 'Prueba', 6, 2022)
    request_nubarium_json(payl)
