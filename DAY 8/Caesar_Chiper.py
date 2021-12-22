logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, plain_shift, plain_direction):
    end_text = ""
    if plain_direction == "decode":
        plain_shift *= -1
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + plain_shift
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {plain_direction}d result: {end_text}")


print(logo)
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26

    caesar(plain_text=text, plain_shift=shift, plain_direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Good Bye")


# def encrypt(plain_text, plain_shift):
#     end_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + plain_shift
#         new_letter = alphabet[new_position]
#         end_text += new_letter
#     print(
#         f"Anda memilih {direction}, maka hasil yang keluar adalah {end_text}")


# def decrypt(plain_text, plain_shift):
#     end_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - plain_shift
#         new_letter = alphabet[new_position]
#         end_text += new_letter
#     print(
#         f"Anda memilih {direction}, maka hasil yang keluar adalah {end_text}")


# if direction == "encode":
#     encrypt(plain_text=text, plain_shift=shift)
# elif direction == "decode":
#     decrypt(plain_text=text, plain_shift=shift)
