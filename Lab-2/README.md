# Лабораторная работа 2
> [!CAUTION]
> В документе к работе после 7 варианта идет 10, так что принял решение 10 вариант считать за 8 и т.д.
> **По этой причине выполнял 15 вариант**.
<div align = "center">
  <img src="https://github.com/user-attachments/assets/22f6436e-d69a-4ab7-bb7e-fc79676e2171" width=500px>
</div>

# Приложение для расчета расхода топлива транспортных средств

## Описание
Это приложение позволяет рассчитывать расход топлива различных видов транспорта в зависимости от их загрузки. Оно включает в себя абстрактный класс `Vehicle`, который содержит общие методы для всех типов транспортных средств, и три его подкласса: `Truck`, `Car` и `Bus`. Каждый из этих классов реализует свои уникальные методы для расчета расхода топлива и стоимости поездки.

## Инструкции по запуску
Для запуска приложения выполните следующие шаги:
1. Установите необходимые библиотеки (`pip install -r requirements.txt`).
2. Скопируйте файл с кодом в ваш проект.
3. Запустите приложение с помощью команды `python main.py`.

## Краткая справка
### Абстрактный класс Vehicle
Этот класс определяет общие методы для всех транспортных средств:
- `__init__`: Конструктор, принимающий параметры расхода топлива и типа топлива.
- `fuel_consumption`: Свойство, возвращающее текущий расход топлива.
- `calculate_fuel_consumption`: Метод для расчета расхода топлива при определенной нагрузке. Реализуется в каждом подклассе индивидуально.
- `calculate_travel_cost`: Метод для расчета стоимости поездки в зависимости от расстояния, цены на топливо и текущего расхода топлива.
- `__str__`: Метод для представления информации о транспортном средстве в строковом виде.

### Класс Truck
Этот класс представляет грузовой автомобиль и наследует свойства и методы от класса `Vehicle`. Дополнительно он имеет свойство `cargo_capacity` и реализует метод `calculate_fuel_consumption`, учитывающий вес груза.
#### Пример создания экземпляра класса

```python
from app.cars_package import Truck

# Создаст объект класса Truck с заданными параметрами
truck = Truck(14.5, "Petrol92", 4000)
```

### Класс Car
Этот класс представляет легковой автомобиль и наследует свойства и методы от класса `Vehicle`. Дополнительно он имеет свойство `passengers` и реализует метод `calculate_fuel_consumption`, учитывающий количество пассажиров.
#### Пример создания экземпляра класса

```python
from app.cars_package import Car

# Создаст объект класса Car с заданными параметрами
car = Car(6.5, "Petrol98", 4) 
```

### Класс Bus
Этот класс представляет автобус и наследует свойства и методы от класса `Vehicle`. Дополнительно он имеет свойство `passenger_capacity` и реализует метод `calculate_fuel_consumption`, учитывающий количество пассажиров.
#### Пример создания экземпляра класса

```python
from app.cars_package import Bus

# Создаст объект класса Bus с заданными параметрами
bus = Bus(11.0, "Diesel", 40) 
```

## Основное приложение
В этом разделе представлена основная логика работы приложения. Здесь происходит инициализация основных классов из пакета `cars_package` и выполнение функций для выбора типа транспортного средства, ввода параметров и расчета стоимости поездки.

#### Функция `main()`
Эта функция управляет основным циклом программы. Пользователь выбирает тип транспортного средства, вводит параметры расхода топлива, типа топлива и вместимости, после чего получает информацию о транспортном средстве и может провести расчет стоимости поездки.

#### Выбор типа транспортного средства
Пользователь может выбрать один из трех типов транспортных средств: автомобиль, грузовик или автобус. Также есть возможность просмотреть список доступных видов топлива и их цен.

#### Функция `get_info()`
Эта функция используется для получения информации о выбранном транспортном средстве и проведения расчета стоимости поездки. Она принимает объект транспортного средства и параметры веса пассажиров или груза, расстояние и тип топлива. После выполнения расчетов результаты могут быть сохранены в формате `.docx` по выбору пользователя.

#### Дополнительные функции
Также добавлены вспомогательные функции для очистки консоли (`console_clear`) и корректной работы на разных операционных системах.

## Тестирование
В этом разделе представлен пример использования модуля `pytest` для тестирования нашего приложения. Проверяется корректность работы методов `calculate_fuel_consumption` и `calculate_travel_cost` для каждого из классов транспортных средств: `Car`, `Truck` и `Bus`. Также добавляются тесты для проверки поведения приложения при вводе неправильных значений.

## Работа в Docker

#### Начало работы

Для начала работы необходимо скачать расширение Docker для вашей IDE/Редактора кода. В моем случае это VSCode. После установки нам предлоэат создать Docker файл, далее выбираем по какому файлу его создать и создаем.
Таким образом у нас автоматически сгенерируется `Dockerfile`. В `requirements.txt` необходимо указать все библиотеки (кроме встроенных).

#### Проблемы с main.py и решение
Просто так положить программу с бесконечным ожиданием ввода в Docker нельзя - вылезает ошибка EOF (end of file). Так что пришлось создать файл `server.py`.
Файл содержит в себе 3 новые библиотеки
```python
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
```
Они нужны, чтобы создать простой сервер, для работы в Docker. Далее создаем перечисление car_type, в котором укажем какой номер соответствует классу автомобиля.
```python
class car_type(Enum):
    car = 1
    bus = 2
    truck = 3
```
После чего создаем класс request который наследуется от BaseModel. Без него работать с запросами не получится =(
  
Далее необходимо создать 2 запроса (можно и один). Первый запрос будет возвращать нам цены на топливо, вид у него будет следующий:
```python
@app.get("/fuel-types/")
def get_fuel_types():
    return {"fuel_types": list(fuel_prices.keys())}
```
Это обычный `GET` запрос, который получает все ключи из листа с ценами и оправляет его по запросу.
  
После создаем основной `POST` запрос, который будет возвращать нам стоимость поездки на машине выбранного нами типа на указанную дистанцию. Его вид следуюзий:
```python
@app.post("/vehicle/")
def calculate_car_cost(request: request):
    vehicle = None
    match request.car_type:
        case car_type.car:
            vehicle = Car(request.fuel_consumption, request.fuel_type, passengers=4)
        case car_type.bus:
            vehicle = Bus(request.fuel_consumption, request.fuel_type, passenger_capacity=4)
        case car_type.truck:
            vehicle = Truck(request.fuel_consumption, request.fuel_type, cargo_capacity=8000)
    fuel_consumption = vehicle.calculate_fuel_consumption(request.weight)
    travel_cost = vehicle.calculate_travel_cost(request.distance, fuel_prices[request.fuel_type], fuel_consumption)
    result = f"Стоимость поездки на автомобиле на {request.distance} км будет стоить {travel_cost:.2f} рублей"
    save_to_sqlite3(vehicle, request.weight, request.distance, request.fuel_type, travel_cost)
    return {"message": result}
```
Он принимает в себя созданный ранее класс, после чего при помощи `match/case` смотрит на переданный ему тип. Использовать `match/case` вроде как не очень хорошо, но в рамках данной работы считаю его использование допустимым. **Важно отметить, что для подсчета стоимости нас не очень интересуют вместимости автомобилей, так что эти параметры заданы по умолчанию.**
 После всех обработок и подсчетов формируется строка и отправляется пользователю в виде `json`.

#### Сборка контейнера и запуск

После всех этих действий в консоль необходимо прописать следующий код:
```commandline
docker build -t lab2-app .  
docker run -p 8000:8000 lab2-app
```
Таким образом мы соберем контейнер из всех файлов в папке (в моем случае папка app). А сразу после сборки запустим контейнер.
Для тестирования сервера я использовал Postman. В нем нам необходимо отправить `POST` запрос на адрес `http://localhost:8000/vehicle/` и передать в `body` json следуещего содержания
```json
{
  "car_type": 2,
  "fuel_consumption": 10.0,
  "fuel_type": "Petrol92",
  "capacity": 5.0,
  "weight": 500.0,
  "distance": 100.0
}
```
Таким образом сервер получает информацию и параметры для расчетов, а в ответ отправит нам строку с результатом подсчета, вид у нее будет такой:
```json
{
    "message": "Стоимость поездки на автомобиле на 100.0 км будет стоить 1356.64 рублей"
}
```