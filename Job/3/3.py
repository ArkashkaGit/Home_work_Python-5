# Задача 3:
#
# Создайте программу для игры в ""Крестики-нолики""

margin = '\t1 | 2 | 3\n\t    —\n\t4 | 5 | 6\n\t    —\n\t7 | 8 | 9\n'

print('Игра в крестики нолики для двоих!\n---------СТАРТ---------\n')
print(margin)
F = 0
while True:
    while F != 1:
        player_X = input('Игрок - X - Введите номер ячейки:\n')

        for i in margin:
            if i == player_X:
                margin = margin.replace(i, 'X')
                player_X = '#'
                print(margin)
                F=1
        if player_X != '#':
            print('Вы ввели не существующую или уже занятую ячейку, попробуйте еще раз!')
    F=0

    if margin[1] =='X' and margin[5] == 'X' and margin[9] == 'X': 
        print('Player -X- WINNER!!!')
        break
    if margin[19] =='X' and margin[23] == 'X' and margin[27] == 'X':
        print('Player -X- WINNER!!!')
        break
    if margin[37] =='X' and margin[41] == 'X' and margin[45] == 'X':
        print('Player -X- WINNER!!!')
        break
    if margin[1] =='X' and margin[19] == 'X' and margin[37] == 'X':
        print('Player -X- WINNER!!!')
        break 
    if margin[5] =='X' and margin[23] == 'X' and margin[41] == 'X':
        print('Player -X- WINNER!!!')
        break 
    if margin[9] =='X' and margin[27] == 'X' and margin[45] == 'X':
        print('Player -X- WINNER!!!')
        break
    if margin[1] =='X' and margin[23] == 'X' and margin[45] == 'X':
        print('Player -X- WINNER!!!')
        break
    if margin[9] =='X' and margin[23] == 'X' and margin[37] == 'X':
        print('Player -X- WINNER!!!')
        break

    while F!=1:
        player_O = input('Игрок - O - Введите номер ячейки:\n')
        for i in margin:
            if i == player_O:
                margin = margin.replace(i, 'O')
                player_O = '#'
                print(margin)
                F=1
        if player_O != '#':
            print('Вы ввели не существующую или уже занятую ячейку, попробуйте еще раз!')
    F=0
        

    if margin[1] =='O' and margin[5] == 'O' and margin[9] == 'O': 
        print('Player -O- WINNER!!!')
        break
    if margin[19] =='O' and margin[23] == 'O' and margin[27] == 'O':
        print('Player -O- WINNER!!!')
        break
    if margin[37] =='O' and margin[41] == 'O' and margin[45] == 'O':
        print('Player -O- WINNER!!!')
        break
    if margin[1] =='O' and margin[19] == 'O' and margin[37] == 'O':
        print('Player -O- WINNER!!!')
        break 
    if margin[5] =='O' and margin[23] == 'O' and margin[41] == 'O':
        print('Player -O- WINNER!!!')
        break 
    if margin[9] =='O' and margin[27] == 'O' and margin[45] == 'O':
        print('Player -O- WINNER!!!')
        break
    if margin[1] =='O' and margin[23] == 'O' and margin[45] == 'O':
        print('Player -O- WINNER!!!')
        break
    if margin[9] =='O' and margin[23] == 'O' and margin[37] == 'O':
        print('Player -O- WINNER!!!')
        break

print('\nКОНЕЦ ИГРЫ, СЫГРАЙТЕ ЕЩЁ РАЗ !!!')
