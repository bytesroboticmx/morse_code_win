#Descripcion:
#Autor:
#Matricula:
#Fecha 18/10/2023

import winsound
import time

# Define el diccionario de caracteres en código Morse
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

def text_to_morse(text):
    text = text.upper()
    morse_message = ''
    for char in text:
        if char in morse_code_dict:
            morse_message += morse_code_dict[char] + ' '
    return morse_message

def play_morse_code(morse_message):
    for symbol in morse_message:
        if symbol == '.':
            winsound.Beep(1000, 100)  # Emite un sonido de 1000 Hz durante 100 ms para el punto
        elif symbol == '-':
            winsound.Beep(1000, 300)  # Emite un sonido de 1000 Hz durante 300 ms para la raya
        elif symbol == ' ':
            time.sleep(0.3)  # Pausa entre letras
        elif symbol == '/':
            time.sleep(1)  # Pausa entre palabras

if __name__ == '__main__':
    message = "Estructura de datos Tequila"
    morse_message = text_to_morse(message)
    print(f"Mensaje en código Morse: {morse_message}")
    play_morse_code(morse_message)
