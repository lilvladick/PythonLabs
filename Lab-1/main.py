import TaskPacket as T

menu = {
        "1. Расстояния между городами": T.one.get_distance(),
        "2. Площадь круга и точка в нем": T.two.solve(),
        "3. Работа с алгеброй": T.three.operationsFunc([1,2,3,4,5]),
        "4. Получение киношек": T.four.search_films('Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'),
        "5. Измерение роста семьи": T.five.solve(),
        "6. Переселение зоопарка": T.six.solve(),
        "7. Песенки": T.six.solve(),
        "8. Расстояния между городами": T.one.get_distance(),
        "9. Расстояния между городами": T.one.get_distance(),
        "10. Расстояния между городами": T.one.get_distance(),
        "11. Расстояния между городами": T.one.get_distance(),
    }

def main():

    while True:
        print("Выберите задание для выполнения:")
        for key in sorted(menu):
            value = menu[key]
            print(f'{key:<30}')
        choice = int(input("\nВыберите задание для выполнения: "))
        if 0<=choice <=len(menu):
            selected_function = menu[list(menu)[choice - 1]]
        else:
            print("Такого номера нет =(")
            break

        selected_function()


if __name__ == "__main__":
        main()