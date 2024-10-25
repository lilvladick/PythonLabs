def multiply_arrays_pairs(list1: [int], list2: [int]):
    """Возвращает generator expression с перемноженными парами чисел из массивов"""
    return (x*y for x, y in zip(list1, list2))

if __name__ == "__main__":
    generator = multiply_arrays_pairs([1, 2, 3 ,4 ,5], [6, 7, 8, 9, 10])

    for _ in range(3):
        print(next(generator))