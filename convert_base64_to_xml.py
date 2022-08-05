import base64


def decode64(encoded_string):
    base64_bytes = encoded_string.encode('UTF-8')
    message_bytes = base64.b64decode(base64_bytes)
    xml_string = message_bytes.decode('UTF-8')
    return xml_string


# def write_xml(xml_string, index):
#     xml_name = f'factura{index}.xml'
#     with open(xml_name, "w", encoding="utf-8") as f:
#         f.write(xml_string)


def main():
    decoded_xml = (decode64('base64_string'))
    write_xml(decoded_xml)


if __name__ == "__main__":
    main()