print('Шифр Цезаря.')
print('Данная программа помогает зашифровать текст, дешифровать текст и подобрать ключ сдвига для дешифровки.')


def cipher(type, key, txt):
    cipher = ''
    if type in 'рус':
        for c in txt:
            if 1040 <= ord(c) <= 1071:  # Верхний регистр русский алфавит
                cipher += chr(ord(c) + key) if 1040 <= ord(c) + key <= 1071 else ''  # работает в обе стороны
                cipher += chr((ord(c) - 1071) + key + 1039) if ord(c) + key > 1071 and ord(c) < 1071 else ''
                cipher += chr(1072 + key + (ord(c) - 1040)) if ord(c) + key < 1040 and ord(c) > 1040 else ''  # разшифровывает
                cipher += chr(1039 + key) if ord(c) == 1071 and action in 'да' else ''  # Шифрует
                cipher += chr(1072 + key) if ord(c) == 1040 and action not in 'да' else ''  # разшифровывает
            elif 1072 <= ord(c) <= 1103:  # нижний регистр русский алфавит
                cipher += chr(ord(c) + key) if 1072 <= ord(c) + key <= 1103 else ''  # работает в обе стороны
                cipher += chr((ord(c) - 1103) + key + 1071) if ord(c) + key > 1103 and ord(c) < 1103 else ''  # Шифрует
                cipher += chr(1104 + key + (ord(c) - 1072)) if ord(c) + key < 1072 and ord(c) > 1072 else ''  # разшифровывает
                cipher += chr(1071 + key) if ord(c) == 1103 and action in 'да' else ''  # Шифрует
                cipher += chr(1104 + key) if ord(c) == 1072 and action not in 'да' else ''  # разштфровывает
            else:
                cipher += c
    else:
        for c in txt:
            if 65 <= ord(c) <= 90:  # Верхний регистр eng алфавит
                cipher += chr(ord(c) + key) if 65 <= ord(c) + key <= 90 else ''  # работает в обе стороны
                cipher += chr((ord(c) - 90) + key + 64) if ord(c) + key > 90 and ord(c) < 90 else ''
                cipher += chr(91 + key + (ord(c) - 65)) if ord(c) + key < 65 and ord(c) > 65 else ''  # разшифровывает
                cipher += chr(64 + key) if ord(c) == 90 and action in 'да' else ''  # Шифрует
                cipher += chr(91 + key) if ord(c) == 65 and action not in 'да' else ''  # разшифровывает
            elif 97 <= ord(c) <= 122:  # нижний регистр eng алфавит
                cipher += chr(ord(c) + key) if 97 <= ord(c) + key <= 122 else ''  # работает в обе стороны
                cipher += chr((ord(c) - 122) + key + 96) if ord(c) + key > 122 and ord(c) < 122 else ''  # Шифрует
                cipher += chr(123 + key + (ord(c) - 97)) if ord(c) + key < 97 and ord(c) > 97 else ''  # разшифровывает
                cipher += chr(96 + key) if ord(c) == 122 and action in 'да' else ''  # Шифрует
                cipher += chr(123 + key) if ord(c) == 97 and action not in 'да' else ''  # разштфровывает
            else:
                cipher += c
    return cipher


def check_txt(txt, type):
    if type == 'lang' and txt in 'eng' or txt in 'рус':
        return txt
    elif type == 'lang':
        while txt not in 'eng' and txt not in 'рус':
            print('Вы ввели недопустимое значения.')
            txt = input('Выберите язык текста. English - eng; Русский - рус: ').lower()
        return txt
    if type == 'action' and (txt in 'да' or txt in 'нет'):
        return txt
    elif type == 'action':
        while txt not in 'да' and txt not in 'нет':
            print('Вы ввели недопустимое значения.')
            txt = input('(Зашифровать текст введите - да, дешифровать - нет): ').lower()
        return txt
    if type == 'key' and (txt in 'да' or txt in 'нет'):
        return txt
    elif type == 'key':
        while txt not in 'да' and txt not in 'нет':
            print('Вы ввели недопустимое значения.')
            txt = input('Если известен ключ, введита - да, если ключ надо найти, введите - нет: ').lower()
        return txt

y = check_txt(input('Выбирете язык текста. English - eng, Русский - рус: ').lower(), 'lang')
s = 31 if y in 'рус' else 25
action = check_txt(input('Требуется зашифровать текст? ("да" или "нет"): ').lower(), 'action')


if action in 'нет':
    if action in 'нет':
        k = int(input('Введите ключ: ')) if check_txt(input('Вам известен ключ? (да - "да"); (нет - "нет"): ').lower(),
                                                      'key') in 'да' else 0
    x = input('Введите текст, который надо дешифровать: ')
    if k == 0:
        while k != -s:
            print(cipher(y, k-1, x), end = ' ')
            k -= 1
            print('Ключ =', k * (-1))
    else:
        print(cipher(y, -k, x))
else:
    k = int(input('Введите ключ: '))
    x = input('Введите текст, который надо зашифровать: ')
    print(cipher(y, k, x))
    


# Создал функцию проверки выбираемых параметров.