"""
Este módulo utiliza la librería ElementTree para obtener
los datos de Concepto, Unidades, Valor Unitario y Total
de un string que representa el contenido de un archivo
XML de una factura.
"""
import xml.etree.ElementTree as ET
from crear_id_unico_concepto import crear_id_unico

# Este es un ejemplo de lo que este módulo necesita para trabajar, es un XML
# en formato de String.
some_xml = '''<cfdi:Comprobante xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital" xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd" Version="3.3" Serie="A" Folio="2751" Fecha="2022-07-29T15:29:58" Sello="fpGjg6U1Cx/98jrIA4882ssClm8xH/2/NtGdJG+wGHhu8/epmV8FvflGc5CGsU31OUm7OJbTuinsSpus9nL65B17lLqh4GYxXQhyUgyNaw9ia6QSmXC5dNJMJ7qZCLue4ytMaQ6eOf7MUqjBRHldLmMXiLJqioeYDtH9nn0YMW0UzlCd/uqbmGxcg2oglYTUBa0YEM8O9pM2MMQyLGktD4b3D2FcOLgyLzkuAh96YFkycfhImf0heNItVbSJsaYSoMfItGbhT6DY+gYB18MqKm1Vb+bWncYqaFg6540f6CWT55ReUoVzx4DrMA4gtp5SjQEH4jgd40V38keYJ2LfBA==" FormaPago="03" NoCertificado="00001000000500354399" Certificado="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" SubTotal="9366.84" Moneda="MXN" Total="9366.84" TipoDeComprobante="I" MetodoPago="PUE" LugarExpedicion="31110">
<cfdi:Emisor Rfc="FIN140930GR6" Nombre="FINANOVA SAPI DE CV SOFOM ENR" RegimenFiscal="601"/>
<cfdi:Receptor Rfc="CAEM800831AE0" Nombre="Miriam Guadalupe Chaparro Estrada" UsoCFDI="G03"/>
<cfdi:Conceptos>
<cfdi:Concepto ClaveProdServ="84101703" NoIdentificacion="84101703" Cantidad="1" ClaveUnidad="E48" Unidad="E48" Descripcion="Intereses devengados del mes de Julio del 2022 MGCHE 28-CT1-25" ValorUnitario="7466.84" Importe="7466.84">
<cfdi:Impuestos>
<cfdi:Traslados>
<cfdi:Traslado Base="7466.84" Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.000000" Importe="0.00"/>
</cfdi:Traslados>
</cfdi:Impuestos>
</cfdi:Concepto>
<cfdi:Concepto ClaveProdServ="84101703" NoIdentificacion="84101703" Cantidad="1" ClaveUnidad="E48" Unidad="E48" Descripcion="Intereses moratorios del mes de Julio del 2022 MGCHE 28-CT1-25" ValorUnitario="1900.00" Importe="1900.00">
<cfdi:Impuestos>
<cfdi:Traslados>
<cfdi:Traslado Base="1900.00" Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.000000" Importe="0.00"/>
</cfdi:Traslados>
</cfdi:Impuestos>
</cfdi:Concepto>
</cfdi:Conceptos>
<cfdi:Impuestos TotalImpuestosTrasladados="0.00">
<cfdi:Traslados>
<cfdi:Traslado Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.000000" Importe="0.00"/>
</cfdi:Traslados>
</cfdi:Impuestos>
<cfdi:Complemento>
<tfd:TimbreFiscalDigital xsi:schemaLocation="http://www.sat.gob.mx/TimbreFiscalDigital http://www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigitalv11.xsd" Version="1.1" UUID="db697930-107a-4186-81e0-2e3b5cc87b03" FechaTimbrado="2022-07-29T16:29:58" RfcProvCertif="LSO1306189R5" SelloCFD="fpGjg6U1Cx/98jrIA4882ssClm8xH/2/NtGdJG+wGHhu8/epmV8FvflGc5CGsU31OUm7OJbTuinsSpus9nL65B17lLqh4GYxXQhyUgyNaw9ia6QSmXC5dNJMJ7qZCLue4ytMaQ6eOf7MUqjBRHldLmMXiLJqioeYDtH9nn0YMW0UzlCd/uqbmGxcg2oglYTUBa0YEM8O9pM2MMQyLGktD4b3D2FcOLgyLzkuAh96YFkycfhImf0heNItVbSJsaYSoMfItGbhT6DY+gYB18MqKm1Vb+bWncYqaFg6540f6CWT55ReUoVzx4DrMA4gtp5SjQEH4jgd40V38keYJ2LfBA==" NoCertificadoSAT="00001000000509846663" SelloSAT="ecDyQAtq65vD+vQXRQxNdA8HWe6I511Vy3v4/dBzUeHznxu4sXCeJUJ8RBAz0cBeC9kpJdmgIMN+4ijRRxQaj4PxchYFU26FCNMxynbv+P8EOzcr6CNeT1WPun8n/nKBKaOMqdGO146I3v7z+1ypcY6Ty7assDOweCyYA/s3lZSMtxd8BU3KrxEH6RlzNJJ/eCGy0CSBsgMSu0JFGielZ7SYXBYxAfVamFZuYwNod7Q7BeEdd4FtkAh/aMa+cILlvUYl0X3SKlsD6hAxXgEldHyv2xE20qUgIgmPpjRVP5bNjvzERl9j89AuJLKSBnvPgH0nIl8qHASc4HaOKw970g=="/>
</cfdi:Complemento>
</cfdi:Comprobante>'''


def process_xml_tree(xml_string, mes, anio, tipo, nombre_cliente):
    temp_list = []
    tree = create_tree(xml_string)
    uuid = get_uuid(tree)
    for index, concepto in enumerate(tree[2]):
        dict_temp = get_concept_info(concepto, mes, anio, tipo, nombre_cliente, uuid, index)
        temp_list.append(dict_temp)
    return temp_list


def get_uuid(tree):
    uuid = tree[4][0].get('UUID')
    return uuid


def create_tree(new_xml_string):
    root = ET.fromstring(new_xml_string)
    return root


def get_concept_info(concepto, mes, anio, tipo, nombre_cliente, uuid, index):
    nombre_cliente = nombre_cliente
    clave = concepto.get('ClaveProdServ')
    cantidad = float(concepto.get('Cantidad'))
    clave_unidad = concepto.get('ClaveUnidad')
    valor_unitario = float(concepto.get('ValorUnitario'))
    importe = float(concepto.get('Importe'))
    id_unico = crear_id_unico(uuid, clave, cantidad, valor_unitario, importe, index)
    dict_temporal = {
        'id': id_unico,
        'nombre_cliente': nombre_cliente,
        'mes': int(mes),
        'anio': int(anio),
        'tipo': tipo,
        'clave_prod_serv': int(clave),
        'prod_serv': None,
        'cantidad': cantidad,
        'clave_unidad': clave_unidad,
        'unidad': None,
        'valor_unitario': valor_unitario,
        'importe': importe,
    }
    return dict_temporal


def main():
    pass


if __name__ == '__main__':
    x = process_xml_tree(some_xml, 6, 2022, 'R', 'Miriam Guadalupe Chaparro Estrada'.upper())
    print(x)
