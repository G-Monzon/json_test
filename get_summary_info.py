"""
Este módulo permite obtener los 3 datos principales del
resumen de facturación obtenido de Nubarium
"""
import json
from decimal import Decimal
from get_base64_xml_lists import get_sent_invoices_xml, get_received_invoices_xml

# Este es un ejemplo de la información que obtendríamos de Nubarium, es un string en formato JSON
ejemplo_json_string = '''{
    "totalEmitidas": "$200,000.14",
    "facturasEmitidas": [
        {
            "folio": "AD405471-340F-4205-B0E5-AC02DA214638",
            "rfcEmisor": "XXXX999999XXX",
            "razonSocialEmisor": "JUAN ALBERTO PEREZ GONZALEZ",
            "rfcReceptor": "XXXX999999XXX",
            "razonSocialReceptor": "LA EMPRESA, S.A. DE C.V.",
            "fechaEmision": "2022-06-01T19:55:50",
            "fechaCertificacion": "2022-06-01T19:56:43",
            "pac": "SAT970701NN3",
            "monto": "$200,000.14",
            "efecto": "Ingreso",
            "estatus": "Cancelable con aceptación",
            "estado": "Vigente",
            "estatusProcesoCancelacion": null,
            "fechaProcesoCancelacion": null,
            "rfcCuentaTerceros": null,
            "motivo": null,
            "folioSustitucion": null,
            "xml": "Base64 del XML 1",
            "pdf": "Base64 del PDF"
        }
    ],
    "totalRecibidas": "$2,795.60",
    "totalDiferencia": "$197,204.54",
    "facturasRecibidas": [
        {
            "folio": "E5ECDC9E-AF7F-4836-A0F8-93C5B9C1769A",
            "rfcEmisor": "XXXX999999XXX",
            "razonSocialEmisor": "BBVA MEXICO, S.A., INSTITUCION DE BANCA MULTIPLE, GRUPO FINANCIERO BBVA MEXICO.",
            "rfcReceptor": "XXXX999999XXX",
            "razonSocialReceptor": "JUAN ALBERTO PEREZ GONZALEZ",
            "fechaEmision": "2022-06-23T01:13:33",
            "fechaCertificacion": "2022-06-23T06:35:01",
            "pac": "CEC961028A98",
            "monto": "$2,795.60",
            "efecto": "Ingreso",
            "estatus": "Cancelable sin aceptación",
            "estado": "Vigente",
            "estatusProcesoCancelacion": null,
            "fechaProcesoCancelacion": null,
            "rfcCuentaTerceros": null,
            "xml": "Base64 del XML 2",
            "pdf": "Base64 del PDF"
        },
        {
            "folio": "E7815AC7-7275-40AA-AD06-4C5B7D27EFA6",
            "rfcEmisor": "XXXX999999XXX",
            "razonSocialEmisor": "BBVA MEXICO, S.A., INSTITUCION DE BANCA MULTIPLE, GRUPO FINANCIERO BBVA MEXICO.",
            "rfcReceptor": "XXXX999999XXX",
            "razonSocialReceptor": "JUAN ALBERTO PEREZ GONZALEZ",
            "fechaEmision": "2022-06-01T02:41:08",
            "fechaCertificacion": "2022-06-01T07:58:18",
            "pac": "CEC961028A98",
            "monto": "$0.00",
            "efecto": "Ingreso",
            "estatus": "Cancelable sin aceptación",
            "estado": "Vigente",
            "estatusProcesoCancelacion": null,
            "fechaProcesoCancelacion": null,
            "rfcCuentaTerceros": null,
            "xml": "Base64 del XML 3",
            "pdf": "Base64 del PDF"
        },
        {
            "folio": "56FD84C7-822C-439F-97AB-50D162E9B277",
            "rfcEmisor": "XXXX999999XXX",
            "razonSocialEmisor": "SEGUROS MONTERREY NEW YORK LIFE SA DE CV",
            "rfcReceptor": "XXXX999999XXX",
            "razonSocialReceptor": "JUAN ALBERTO PEREZ GONZALEZ",
            "fechaEmision": "2022-06-01T10:09:40",
            "fechaCertificacion": "2022-06-01T10:09:41",
            "pac": "ASE0201179X0",
            "monto": "$0.00",
            "efecto": "Pago",
            "estatus": "Cancelable sin aceptación",
            "estado": "Vigente",
            "estatusProcesoCancelacion": null,
            "fechaProcesoCancelacion": null,
            "rfcCuentaTerceros": null,
            "xml": "Base64 del XML 4",
            "pdf": "Base64 del PDF"
        }
    ],
    "estatus": "OK",
    "claveMensaje": 0,
    "codigoValidacion": "gf1657073270.0487676"
}'''


def summary_from_file(json_filepath):
    """
    Convierte un archivo JSON a Python.
    Toma como único parámetro el string del filepath del archivo JSON.
    """
    with open(json_filepath, 'r') as f:
        json_text = json.load(f)
        return json_text


def summary_from_string(json_string):
    """
    Convierte un String de JSON a Python.
    Su único parámetro acepta un String que contenga los datos de Nubarium
    de "Get invoices from SAT with CIEC".
    """
    json_text = json.loads(json_string)
    return json_text


def get_summary(text):
    """
    Devuelve en 3 variables de tipo Decimal el total de las facturas en forma
    de un diccionario, ejemplo:

    dict_resumen = {
        'totalEmitidas': Total de facturación emitida en el mes,
        'totalRecibidas': Total de facturación recibida en el mes,
        'totalDiferencia': Total de la diferencia (emitida - recibida)
    }

    Decimal permite precisión mejorada para valores monetarios.
    Del JSON se obtienen los datos en Strings, se eliminan los '$' y las comas.
    """
    total_emitidas = Decimal((text['totalEmitidas']).replace('$', '').replace(',', ''))
    total_recibidas = Decimal((text['totalRecibidas']).replace('$', '').replace(',', ''))
    total_diferencia = Decimal((text['totalDiferencia']).replace('$', '').replace(',', ''))
    dict_resumen = {
        'totalEmitidas': total_emitidas,
        'totalRecibidas': total_recibidas,
        'totalDiferencia': total_diferencia
    }
    return dict_resumen


def main():
    """
    Se descomenta uno de los "json_convertido" que se va a utilizar realmente,
    o se usa una archivo JSON o un string.
    Por "default" se emplea el JSON en string, si se va a emplear un archivo
    JSON se debe de comentar la línea que llama a la función
    "summary_from_string" y se debe de descomentar la línea que llama
    a la función "summary_from_file".
    """
    # json_convertido = summary_from_file('./ejemplo_facturas_nubarium.JSON')
    json_convertido = summary_from_string(ejemplo_json_string)
    get_summary(json_convertido)
    lista_emitidas = get_sent_invoices_xml(json_convertido)
    listas_recibidas = get_received_invoices_xml(json_convertido)
    print(f'Lista de XML de facturas recibidas: {listas_recibidas}')
    print(f'Lista de XML de facturas emitidas: {lista_emitidas}')


if __name__ == '__main__':
    main()
