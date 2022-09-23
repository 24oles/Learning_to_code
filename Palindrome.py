# объявление функции
def is_palindrome(text):
    text_str = ''
    text = [text[i].lower() for i in range(len(text)) if text[i].lower().isalpha()]
    for i in text:
        text_str += i
    x = len(text_str)
    if text_str[:] == text_str[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))