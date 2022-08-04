"""Este módulo devuelve 2 listas de strings en Base64 donde se contienen los XML de las facturas cuando es llamado"""

received_list = []
sent_list = []


def get_received_invoices_xml(json_text):
    for invoice in json_text['facturasRecibidas']:
        received_list.append(invoice['xml'])
    return received_list


def get_sent_invoices_xml(json_text):
    for invoice in json_text['facturasEmitidas']:
        sent_list.append(invoice['xml'])
    return sent_list


if __name__ == '__main__':
    pass
