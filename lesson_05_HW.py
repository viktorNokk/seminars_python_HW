# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input()
text = text.split()
new_text = list(filter(lambda i: 'абв' not in i, text))
print(new_text)

# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
    
def encode(data):
    encoding = ''
    prev_symbol = ''
    count = 0
    for symbol in data:
        if symbol != prev_symbol:
            if prev_symbol:
                encoding += str(count) + prev_symbol
            count = 1
            prev_symbol = symbol
        else:
            count += 1
    else:
        encoding += str(count) + prev_symbol
        return encoding

def decode(data):
    decoding = ''
    count = ''
    for symbol in data:
        if symbol.isdigit():
            count += symbol
        else:
            decoding += symbol * int(count)
            count = ''
    return decoding

encode_result = encode('aaaaassssdddfffggghhhjjkkl')
print(f'Encoding result: {encode_result}')

decode_result = decode('3a5f2s2d5f8t')
print(f'Decoding result {decode_result}')

# 3. Игра "крестики-нолики"

from colorama import Fore
# init(autoreset=True)

field = list(range (1, 10))

def draw(field):
    print(Fore.GREEN + '-------------')
    for i in range(3):
        print(Fore.GREEN + '|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], '|')
        print(Fore.GREEN + '-------------')

def victory(field):
    win_positions = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in win_positions:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False

def player_input(X_or_O):
    valid = False
    while not valid:
        player_in = input('Input position ' + X_or_O + ': ')
        try:
            player_in = int(player_in)
        except:
            print('Incorrect input! Input the digit')
            continue
        if player_in >= 1 and player_in <= 9:
            if(str(field[player_in - 1]) not in 'XO'):
                field[player_in - 1] = X_or_O
                valid = True
            else:
                print('This field is already busy!')
        else:
            print('Incorrect input, try again')

def main(field):
    count = 0
    win = False
    while not win:
        draw(field)
        if count % 2 == 0:
            player_input(Fore.RED + 'X')
        else:
            player_input(Fore.BLUE + 'O')
        count += 1
        if count > 4:
            temp = victory(field)
            if temp:
                print(temp, '- Win!')
                win = True
                break
        if count == 9:
            print('Game draw')
            break
        draw(field)
main(field)






















#draw(field)
