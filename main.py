koloda = [6,7,8,9,10,2,3,4,11] * 4

import random
random.shuffle(koloda)

print('Игра в 21-одно')
count = 0
while True:
    choise = input('Будете брать карту? Да/Нет\n')
    if choise == 'Да':
        current = koloda.pop()
        if current == 11:
            print("Вам выпал туз (11 очков)")
            count += current
        elif current == 4:
            print("Ваv выпал король (4 очка)")
            count += current
        elif current == 3:
            print('Вам выпала дама (3 очка)')
            count += current
        elif current == 2:
            print('Вам выпал валет (2 очка)')
            count += current
        else:
            print('Вам попалась карта достоинством %d' % current)
            count += current
        if count > 21:
            print('Извините, но вы проиграли')
            if 21 < count < 25:
                print(f'Вы набрали {count} очка.')
            elif count >= 25:
                print(f'Вы набрали {count} очков.')
            print('До новых встреч!')
            break
        elif count == 21:
            print('Поздравляю вы набрали 21!')
            print('До новых встреч!')
            break
        else:
            print('У вас %d очков.' % count)
    elif choise == 'Нет':
        print('У вас %d очков и вы закончили игру.' % count)
        print('До новых встреч!')
        break

