txt = input()
spisok_slov = txt.split() # текст разделен на слова по пробелам
decode_string = []

# функция определяет длину слова
def dlina_slova(slovo):
    dlina_slova = 0
    for i in slovo:
        if i.isalpha():
            dlina_slova += 1
    return dlina_slova

# функция создает новое слово используя размера по функции dlina_slova
def new_word(word):
    n = dlina_slova(word) # размер сдвига
    shifr = ''
    for i in word:
        if 97 <= ord(i) <= 122: # является ли эта буква в диапазоне маленьких букв
            if ord(i) + n > 122:  # если смещение превышает длину алфавита
                shifr += chr(ord(i) - 26 + n) # начать счет сначала
            else:
                shifr += chr(ord(i) + n)
        elif 65 <= ord(i) <= 90:
            if ord(i) + n > 90:
                shifr += chr(ord(i) - 26 + n)
            else:
                shifr += chr(ord(i) + n)
        else:
            shifr += i
    return shifr

# обрабатывая каждое слово - формируем новую строку
for i in spisok_slov:
    decode_string.append(new_word(i))
print(*decode_string)