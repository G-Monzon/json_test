"""
Buscar validar los campos de RFC, de password, de meses y de años ¿en el front end? ¿O usar Regex?
A de momento lo tengo funcionando con un JSON String de ejemplo para poder obtener los datos
y mandarlos al módulo de Pandas.

Este es el módulo que debe recibir los valores de rfc (str), password (str), una lista de
meses (ints) y una lista de años (ints) para hacer las peticiones a Nubarium. Cada mes es
una petición y se obtendrán los datos relevantes de la facturación de cada mes (a cada conjunto
de datos lo llamo "concepto"). Cada concepto es un diccionario y todos los conceptos se van
a guardar en una lista de diccionarios (una lista de conceptos); dicha lista será enviada al
módulo de Pandas para su procesamiento.

Falta resolver qué pasa si no hay facturación en un determinado mes y año (revisar error de
petición en Nubarium) y ver cómo hacer una petición masiva (Ej. Todos los meses de los últimos
10 años o algo similar).

Debo asegurarme de que si no existe facturación en determinado mes (error de petición),
no se agregue información al dataframe. La otra opción es llenar de None los valores vacíos (lo
veo innecesario, pero es opción).
WIP
"""
from crear_lista_conceptos_de_un_mes import crear_lista_conceptos_mes
from request_nubarium_json import solicitar_facturacion_mes


# Desde el front se debe de poder seleccionar el rango de meses y años, y el rfc y password
rfc_ejemplo = 'XXXXXX'  # Debe ser un String que contenga un RFC válido
password_ejemplo = 'YYYYYY'  # Debe ser un String que contenga el password correcto
meses_ejemplo = [6]  # Debe ser una lista, al menos debe incluir un mes
anios_ejemplo = [2022]  # Debe ser una lista, al menos debe incluir un año


def crear_lista_conceptos_cliente(rfc, password, meses, anios):
    lista_conceptos_cliente = []
    for anio in sorted(anios):
        for mes in sorted(meses):
            nubarium_json = solicitar_facturacion_mes(rfc, password, mes, anio)
            lista_un_mes = crear_lista_conceptos_mes(nubarium_json, mes, anio)
            for concepto in lista_un_mes:
                lista_conceptos_cliente.append(concepto)
    return lista_conceptos_cliente


if __name__ == '__main__':
    to_pandas = crear_lista_conceptos_cliente(
        rfc_ejemplo,
        password_ejemplo,
        meses_ejemplo,
        anios_ejemplo,
    )
    # for x in to_pandas:
    #     print(x)
