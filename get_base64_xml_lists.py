"""
Este módulo contiene las funciones necesarias para generar
2 listas de strings en Base64 donde se contienen
los XML de las facturas del JSON proporcionado (debe ya estar
leído por Python usando json.load() o json.loads()).
"""


def get_received_invoices_xml(json_text):
    """
    Esta función recibe el JSON de Python y devuelve una lista que contiene
    los XML en formato base64 de las facturas recibidas del mes.
    :param json_text: Python object (diccionario en este caso).
    :return: list
    """
    received_list = []
    for invoice in json_text['facturasRecibidas']:
        received_list.append(invoice['xml'])
    return received_list


def get_sent_invoices_xml(json_text):
    """
    Esta función recibe el JSON de Python y devuelve una lista que contiene
    los XML en formato base64 de las facturas emitidas del mes.
    :param json_text: Python object (diccionario en este caso).
    :return: list
    """
    sent_list = []
    for invoice in json_text['facturasEmitidas']:
        sent_list.append(invoice['xml'])
    return sent_list


if __name__ == '__main__':
    pass
