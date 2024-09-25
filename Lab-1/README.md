# Лабораторная работа 1
## Список заданий:
1. **`00_distance.py`**
   - **Задача:** Составим словарь словарей расстояний между ними
   - **Реализация:**
     ```python
     for i in sites:
        distances[i] = {}
        for j in sites:
            if i != j:
                x1, y1 = sites[i]
                x2, y2 = sites[j]
    
                distance = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
                distances[i][j] = distance


     print(distances)
     ```

2. **`01_circle.py`**
   - **Задача:** 
     - Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
     - Если точка point лежит внутри того самого круга, то выведите на консоль True, Или False, если точка лежит вовне круга.
     - Аналогично для другой точки
   - **Реализация:**
     ```python
     print(round(radius*3.1415926, 4))
     print(point_1[0]**2 + point_1[1]**2 <= radius**2)
     print(point_2[0]**2 + point_2[1]**2 <= radius**2)
     ```

3. **`02_operations.py`**
   - **Задача:** Расставьте знаки операций "плюс", "минус", "умножение" и скобки между числами "1 2 3 4 5" так, что бы получилось число "25"
   - **Реализация:**
     ```python
     print(1*2+3+4*5)
     ```

4. **`03_my_favorite_movies.py`**
   - **Задача:** 
     - Выведите на консоль с помощью индексации строки, последовательно:
       - первый фильм 
       - последний 
       - второй 
       - второй с конца
   - **Реализация:**
     ```python
     first = my_favorite_movies[0:10]
     last = my_favorite_movies[42:57]
     second = my_favorite_movies[12:25]
     second_last = my_favorite_movies[35:40]
    
     print(first+",\n"+last+",\n"+second+",\n"+second_last)
     ```

5. **`04_my_family.py`**
   - **Задача:** 
     - Выведите на консоль рост отца в формате "Рост отца - ХХ см"
     - Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
   - **Реализация:**
     ```python
     print(f"Рост отца - {my_family_height[0][1]} см")
     sum = 0
     for i in my_family_height:
         sum+=i[1]
     print("Общий рост моей семьи - "+str(sum)+" см")
     ```

6. **`05_zoo.py`**
   - **Задача:** 
     - Посадите медведя (bear) между львом и кенгуру
     - Добавьте птиц из списка birds в последние клетки зоопарка
     - Уберите слона
     - Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
   - **Реализация:**
     ```python
     zoo.insert(1, 'bear')
     print(zoo)
     zoo.extend(birds)
     print(zoo)
     zoo.remove('elephant')
     print(zoo)
     print(str(zoo.index('lion')+1) , str(zoo.index('lark')+1))
     ```

7. **`06_songs_list.py`**
   - **Задача:** 
     - Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате.
     - Распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
   - **Реализация:**
     ```python
     violator_songs_map = {song[0]: song[1] for song in violator_songs_list}
     time1 = violator_songs_map['Halo'] + violator_songs_map['Enjoy the Silence'] + violator_songs_map['Clean']
     print(f"Три песни звучат {time1:.2f} минут")
     
     time2 = 0
     time2+=violator_songs_dict['Sweetest Perfection'] + violator_songs_dict['Blue Dress'] + violator_songs_dict['Policy of Truth']
     print(f"А другие три песни звучат {round(time2)} минут")
     ```

8. **`07_secret.py`**
   - **Задача:** Расшифровать заданный шифр следую подсказкам.
   - **Реализация:**
     ```python
     one_w = secret_message[0][3]
     two_w = secret_message[1][9:13]
     three_w = secret_message[2][5:15:2]
     four_w = secret_message[3][12:6:-1]
     five_w = secret_message[4][20:15:-1]
     
     result = one_w + " " + two_w + " " + three_w + " " + four_w + " " + five_w
     print(result)
     ```

9. **`08_garden.py`**
   - **Задача:** 
     - Создайте множество цветов, произрастающих в саду и на лугу
     - Выведите на консоль все виды цветов
     - Выведите на консоль те, которые растут и там и там
     - Выведите на консоль те, которые растут в саду, но не растут на лугу
     - Выведите на консоль те, которые растут на лугу, но не растут в саду
   - **Реализация:**
     ```python
     garden_set = set(garden)
     meadow_set = set(meadow)
    
     all_flowers = garden_set.union(meadow_set)
     print(", ".join(all_flowers))
    
     gm_flowers = garden_set & meadow_set
     print(", ".join(gm_flowers))
    
     u_garden_flowers = garden_set - meadow_set
     print(", ".join(u_garden_flowers))
    
     u_meadow_flowers = meadow_set - garden_set
     print(", ".join(u_meadow_flowers))
     ```
10. **`09_shopping.py`**
    - **Задача:** Создайте словарь цен на продукты следующего вида (писать прямо в коде).
    - **Реализация:**
      ```python
      sweets = {
        'печенье': [
            {'shop': 'ашан', 'price': 10.99},
            {'shop': 'пятерочка', 'price': 9.99}
        ],
        'конфеты': [
            {'shop': 'пятерочка', 'price': 32.99},
            {'shop': 'магнит', 'price': 30.99},
        ],
        'карамель': [
            {'shop': 'ашан', 'price': 45.99},
            {'shop': 'магнит', 'price': 41.99},
        ],
        'пирожное': [
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.99},
        ]
      }
      ```
     
11. **`10_store.py`**
    - **Задача:** Вывести стоимость каждого вида товара на складе.
    - **Реализация:**
      ```python
      table_code = goods['Стол']
      tables_quantity = store[table_code][0]['quantity'] + store[table_code][1]['quantity']
      tables_cost = (store[table_code][0]['quantity'] * store[table_code][0]['price']
                    + store[table_code][0]['quantity'] + store[table_code][1]['price'])
      print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')
      
      sofa_code = goods['Диван']
      sofas_quantity = store[sofa_code][0]['quantity'] + store[sofa_code][1]['quantity']
      sofas_cost = (store[sofa_code][0]['quantity'] * store[sofa_code][0]['price']
                    + store[sofa_code][0]['quantity'] + store[sofa_code][1]['price'])
      print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')
      
      chair_code = goods['Стул']
      chairs_quantity = store[chair_code][0]['quantity'] + store[chair_code][1]['quantity'] + store[chair_code][2]['quantity']
      chairs_cost = (store[chair_code][0]['quantity'] * store[chair_code][0]['price'] +
                     store[chair_code][1]['quantity'] * store[chair_code][1]['price'] +
                     store[chair_code][2]['quantity'] * store[chair_code][2]['price'])
      print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')
      ```
