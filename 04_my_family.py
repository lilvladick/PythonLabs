#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Отец', 180],
    ['Мать', 165],
    ['Я', 175],
    ['Брат', 185],
    ['Сестра', 160],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
sum = 0
for i in my_family_height:
    sum+=i[1]
    print(i[0] + " - " + str(i[1])+" см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print(str(sum)+" см")