#Author: Mateus Pimenta
#2020
fonte = {'A': 0b11000, 'B': 0b10011, 'C': 0b01110, 'D': 0b10010, 'E': 0b10000, 'F': 0b10110, 'G': 0b01011,
         'H': 0b00101, 'I': 0b01100, 'J': 0b11010, 'K': 0b11110, 'L': 0b01001, 'M': 0b00111, 'N': 0b00110,
         'O': 0b00011, 'P': 0b01101, 'Q': 0b11101, 'R': 0b01010, 'S': 0b10100, 'T': 0b00001, 'U': 0b11100,
         'V': 0b01111, 'W': 0b11001, 'X': 0b10111, 'Y': 0b10101, 'Z': 0b10001, '9': 0b00100, '8': 0b11111,
         '+': 0b11011, '4': 0b01000, '3': 0b00010, '/': 0b00000}
especiais = {' ': '9', '?': '8', '.': '+', ',': '3', '!': '4', ';': '/'}

texto = input('Digite a frase').upper()

chave = 'KROM'
listaChave = []
resultado = []
carA = []
carB = []

for char in chave:
    while len(texto) > len(chave):
        chave += char

def cripto(texto, chave):
    indice = 0
    textofin = ''
    newtexto = ''
    for letra in texto:
        if letra in especiais.keys():
            newtexto += especiais[letra]
        else:
            newtexto += letra
    [[carA.append(value) for key, value in fonte.items() if letra == key] for letra in newtexto]
    [[carB.append(value) for key, value in fonte.items() if char == key] for char in chave]

    while len(resultado) < len(texto):
        resultado.append(carA[indice] ^ carB[indice])
        indice += 1

    for valor in resultado:
        for k, v in fonte.items():
            if v == valor:
                textofin += k
    return textofin

def decripto():
    newtexto = ''

    for letra in cripto(texto, chave):
        if letra in especiais.values():
            for key, valor in especiais.items():
                if letra == valor:
                    newtexto += key
        else:
            newtexto += letra

    return newtexto

print('Texto Criptografado: ', cripto(texto, chave))
print('Texto Decifrado: ', decripto())

