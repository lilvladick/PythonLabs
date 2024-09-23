#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

#zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
def new_animal(zoo: list, index:int, animal: str):
    zoo.insert(index, animal)
    return zoo

print(new_animal(['lion', 'kangaroo', 'elephant', 'monkey', ], 1, 'bear'))

# добавьте птиц из списка birds в последние клетки зоопарка
#birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код

def new_animals(zoo: list, animals: list):
    zoo.extend(animals)
    return zoo
print(new_animals(['lion', 'kangaroo', 'elephant', 'monkey', ], ['rooster', 'ostrich', 'lark', ]))
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код

def free_the_beast(zoo: list, animal: str):
    zoo.remove(animal)
    return zoo

print(free_the_beast(['lion', 'kangaroo', 'elephant', 'monkey', ], 'elephant'))
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код

def get_animal_index_but_for_normal_peoples(zoo: list, animal:str):
    return zoo.index(animal) + 1


zooooo = ['lion', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']
print(str(get_animal_index_but_for_normal_peoples(zooooo, 'lion')) , str(get_animal_index_but_for_normal_peoples(zooooo, 'lark')))

def solve():
    print(new_animal(['lion', 'kangaroo', 'elephant', 'monkey', ], 1, 'bear'))
    print(new_animals(['lion', 'kangaroo', 'elephant', 'monkey', ], ['rooster', 'ostrich', 'lark', ]))
    print(free_the_beast(['lion', 'kangaroo', 'elephant', 'monkey', ], 'elephant'))
    print(str(get_animal_index_but_for_normal_peoples(zooooo, 'lion')),
          str(get_animal_index_but_for_normal_peoples(zooooo, 'lark')))