def inverter_string(string):
    invertida = ""
    for char in string:
        invertida = char + invertida
    return invertida


entrada = input("Digite uma string: ")
resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")