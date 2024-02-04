# # # TITLE: Text to Morse Code converter # # #

morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '-.-.',
    'K': '.---',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' / ',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}


def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~TEXT TO MORSE CODE CONVERTER~~~~~~~~~~~~~~~~~~~~~~~~")
    phrase = input("Text: ").upper()
    print(change_morse(phrase.strip()))


def change_morse(word):
    output = ""
    for char in word:
        char = morse[char]
        output += f" {char}"

    return output.strip()


if __name__ == '__main__':
    main()
