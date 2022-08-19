import json
nums_m = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
letters_m = [
    '.-',
    '-...',
    '-.-.',
    '-..',
    '.',
    '..-.',
    '--.',
    '....',
    '..',
    '.---',
    '-.-',
    '.-..',
    '--',
    '-.',
    '---',
    '.--.',
    '--.-',
    '.-.',
    '...',
    '-',
    '..-',
    '...-',
    '.--',
    '-..-',
    '-.--',
    '--..',
]
symbols_m = [
    '. -.-.-',
    '--..--',
    '..--..',
    '.----.',
    '-.-.--',
    '-..-.',
    '-.--.',
    '-.--.-',
    '.-...',
    '---...',
    '-.-.-.',
    '-... -',
    '.-.-.',
    '-.... -',
    '..--.-',
    '.-..-.',
    '... -..-',
    '.--.-.',
    '..-.-',
    '--... -',
    '/'
]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
symbols = ['.', ',', '?', "'", '!', '/', '(', ')', '&', ':', ';', '=', '+', '-', '_', '"', '$', '@', '¿', '¡'," "]
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alphanumerics = letters + nums + symbols
alphanumerics_m = letters_m + nums_m + symbols_m

alpha_dict = {alphanumerics[i]: alphanumerics_m[i] for i in range(len(alphanumerics_m))}
code_dict = {alphanumerics_m[i]:alphanumerics[i] for i in range(len(alphanumerics_m))}

with open("code.json" ,"w") as file:
    json.dump({"text":alpha_dict,"morse":code_dict},file,indent=4)