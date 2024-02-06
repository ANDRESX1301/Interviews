# Definimos una función llamada contar_secuencias_no_repetitivas
def contar_secuencias_no_repetitivas(cadena):
    # Inicializamos el contador a 0 y la longitud de la secuencia actual a 1
    contador = 0
    secuencia_actual = 1

    # Iteramos sobre la cadena, comenzando desde el segundo carácter (índice 1)
    for i in range(1, len(cadena)):
        # Verificamos si el carácter actual es diferente al anterior
        if cadena[i] == cadena[i - 1]:
            print('[i]', i, 'c[i]', cadena[i], 'c[i-1]', cadena[i - 1])
            # Si es diferente, incrementamos la longitud de la secuencia actual
            secuencia_actual += 1
            print('secuencia_actual', secuencia_actual)
        else:
            # Si es igual, incrementamos el contador y reiniciamos la secuencia actual a 1
            print('pasa por el else', contador )
            contador += 1
            secuencia_actual = 1
            print('pasa por el else',contador)

    # Asegurarse de contar la última secuencia si existe
    contador += 1

    # Devolvemos el resultado final
    return contador

# Solicitamos al usuario que ingrese una cadena
entrada_usuario = input("Ingresa una cadena: ")

# Calculamos el resultado llamando a la función contar_secuencias_no_repetitivas con la entrada del usuario
resultado = contar_secuencias_no_repetitivas(entrada_usuario)

# Mostramos el resultado
print(f"Secuencias no repetitivas en '{entrada_usuario}': {resultado}")