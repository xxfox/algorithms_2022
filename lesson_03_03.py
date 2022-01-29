"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

from hashlib import sha256
word = 'papa'
result = set()

for i in range(len(word)):
    for j in range(len(word) + 1):
        if word[i:j+i+1] != word[:]:
            sub_string = word[i:j + i + 1]
            result.add(sha256(sub_string.encode()).hexdigest())
print(f'В строке {word} найдено {len(result)} уникальных подстрок')
