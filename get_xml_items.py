"""
Este módulo utiliza la librería ElementTree para obtener
los datos de Concepto, Unidades, Valor Unitario y Total
de un string que representa el contenido de un archivo
XML de una factura.
"""
import xml.etree.ElementTree as ET


def create_tree(xml_string):
    tree = ET.ElementTree(ET.fromstring(xml_string))
    print(tree)


def main():
    pass


if __name__ == '__main__':
    main()
