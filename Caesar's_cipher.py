print('Шифр Цезаря.')
print('Данная программа помогает зашифровать текст, дешифровать текст и подобрать ключ для дешифровки.')


def cipher(type, key, txt):
    cipher = ''
    if type == 'рус':
        for c in txt:
            if 1040 <= ord(c) <= 1071:  # Верхний регистр русский алфавит
                cipher += chr(ord(c) + key) if 1040 <= ord(c) + key <= 1071 else ''  # работает в обе стороны
                cipher += chr((ord(c) - 1071) + key + 1039) if ord(c) + key > 1071 and ord(c) < 1071 else ''
                cipher += chr(1072 + key + (ord(c) - 1040)) if ord(c) + key < 1040 and ord(c) > 1040 else ''  # разшифровывает
                cipher += chr(1039 + key) if ord(c) == 1071 and action in 'y' else ''  # Шифрует
                cipher += chr(1072 + key) if ord(c) == 1040 and action not in 'y' else ''  # разшифровывает
            elif 1072 <= ord(c) <= 1103:  # нижний регистр русский алфавит
                cipher += chr(ord(c) + key) if 1072 <= ord(c) + key <= 1103 else ''  # работает в обе стороны
                cipher += chr((ord(c) - 1103) + key + 1071) if ord(c) + key > 1103 and ord(c) < 1103 else ''  # Шифрует
                cipher += chr(1104 + key + (ord(c) - 1072)) if ord(c) + key < 1072 and ord(c) > 1072 else ''  # разшифровывает
                cipher += chr(1071 + key) if ord(c) == 1103 and action in 'y' else ''  # Шифрует
                cipher += chr(1104 + key) if ord(c) == 1072 and action not in 'y' else ''  # разштфровывает
            else:
                cipher += c
    else:
        for c in txt:
            if 65 <= ord(c) <= 90:  # Верхний регистр eng алфавит
                cipher += chr(ord(c) + key) if 65 <= ord(c) + key <= 90 else ''  # работает в обе стороны
                cipher += chr((ord(c) - 90) + key + 64) if ord(c) + key > 90 and ord(c) < 90 else ''
                cipher += chr(91 + key + (ord(c) - 65)) if ord(c) + key < 65 and ord(c) > 65 else ''  # разшифровывает
                cipher += chr(64 + key) if ord(c) == 90 and action in 'y' else ''  # Шифрует
                cipher += chr(91 + key) if ord(c) == 65 and action not in 'y' else ''  # разшифровывает
            elif 97 <= ord(c) <= 122:  # нижний регистр eng алфавит
                cipher += chr(ord(c) + key) if 97 <= ord(c) + key <= 122 else ''  # работает в обе стороны
                cipher += chr((ord(c) - 122) + key + 96) if ord(c) + key > 122 and ord(c) < 122 else ''  # Шифрует
                cipher += chr(123 + key + (ord(c) - 97)) if ord(c) + key < 97 and ord(c) > 97 else ''  # разшифровывает
                cipher += chr(96 + key) if ord(c) == 122 and action in 'y' else ''  # Шифрует
                cipher += chr(123 + key) if ord(c) == 97 and action not in 'y' else ''  # разштфровывает
            else:
                cipher += c
    return cipher

y = input('Введите язык шифра, eng или рус: ')
s = 33 if y == 'рус' else 27
action = input('''Выбирете дейтсвие:
Зашифровать? (да: "y", нет: "n"): ''')


if action == 'n':
    k = int(input('Введите ключ: ')) if input('Нам известен ключ? (да - "y"); (нет - "n"): ') == 'y' else 0
    x = input('Введите текст, который надо дешифровать: ')
    if k == 0:
        while k != s:
            print(k)
            print(cipher(y, -k, x))
            k += 1
    else:
        print(k)
        print(cipher(y, -k, x))
else:
    k = int(input('Введите ключ: '))
    x = input('Введите текст, который надо зашифровать: ')
    print(x)
    print(cipher(y, k, x))


