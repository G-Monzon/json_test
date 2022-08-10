"""
Algoritmo para crear un ID único para cada concepto, a partir de los datos de cada concepto
individual. Esto con la intención de poder utilizar el campo de "id"
como primary key en la tabla de conceptos de todos los clientes y asegurarse de que no se repitan.
"""


def crear_id_unico(uuid, clave, cantidad, valor_unitario, importe, index):
    cantidad, valor_unitario, importe = abs(cantidad), abs(valor_unitario), abs(importe)
    val = int(clave[-1])
    min_index, max_index = 48, 79
    iteracion = index // 79
    index = int(index + min_index - (max_index * iteracion))
    if cantidad > 1:
        cant = len(str(int(cantidad)))
        cantidad = (cantidad/10**(cant-1))
    else:
        cantidad += (val * cantidad) + 1
    if valor_unitario > 1:
        unit = len(str(int(valor_unitario)))
        valor_unitario = valor_unitario / 10 ** (unit - 1)
    else:
        valor_unitario += (val * valor_unitario) + 1
    if importe > 1:
        imp = len(str(int(importe)))
        importe = importe / 10 ** (imp - 1)
    else:
        importe += (val * importe) + 1
    num_unico = int(clave) + (valor_unitario*10**7) + (cantidad*10**6) + (importe*10**3)
    if len(str(int(num_unico))) == 8:
        num_unico = str(int(num_unico*10))
    elif len(str(int(num_unico))) == 9:
        num_unico = str(int(num_unico))
    # print(f'El num único tiene {len(str(num_unico))} números, con un valor de {num_unico}')
    ascii_index = chr(index)
    id_unico = uuid + '-' + str(num_unico) + '-' + ascii_index
    # print(id_unico)
    return id_unico


if __name__ == '__main__':
    crear_id_unico('uuid', '12345678', 12.5, 100, 1250, 0)

# Menor es
# 1010101

# Mayor es
# 95141904
