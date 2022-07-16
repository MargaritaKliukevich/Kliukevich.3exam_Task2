# 2. Напишите функцию, которая возвращает True, если введенный текст читается одинаково слева-направо и справа-налево.
# Иначе – False.

def polindrom(a):
    if a == a[::-1]:
        return True
    else:
        return False
print(polindrom(input('Введите текст: ')))