import pyperclip

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


def get_letter(val):
    for key, value in MORSE_CODE_DICT.items():
        if val == value:
            return key

    return " "


def encode(text):
    morse_code = ""

    for letter in text:
        if letter == ",":
            morse_code += MORSE_CODE_DICT[", "]
        elif letter == " ":
            morse_code += "/"
        else:
            morse_code += MORSE_CODE_DICT[letter.upper()] + " "

    print(morse_code)
    pyperclip.copy(morse_code)


def decode(morse):
    text = ""
    morse_list = morse.split(" ")

    for code in morse_list:
        text += get_letter(code)

    print(text)


text_or_morse = input("Type 1 to text, 2 for morse code: ")
if text_or_morse == "1":
    user_text = input("Type your text: ")
    
    encode(user_text)
elif text_or_morse == "2":
    user_morse = input("Type your morse code: ")
    decode(user_morse)
else:
    print("Wrong input")