import flet as ft
from flet import TextField, ElevatedButton, Column, Text, Tab, Tabs
from lab4_solution import modules, multiply_arrays_pairs, generate_passwords

def main(page: ft.Page):
    a_field = TextField(label="Начало диапазона (a)")
    b_field = TextField(label="Конец диапазона (b)")
    modules_result = Text()

    def on_modules_click(e):
        try:
            a = int(a_field.value)
            b = int(b_field.value)
            result = modules(a, b)
            modules_result.value = f"Результат: {result}"
        except ValueError as ex:
            modules_result.value = str(ex)
        modules_result.update()

    modules_tab_content = Column([
        a_field, b_field,
        ElevatedButton("Получить модули", on_click=on_modules_click),
        modules_result
    ])

    list1_field = TextField(label="Первый список чисел (через запятую)")
    list2_field = TextField(label="Второй список чисел (через запятую)")
    multiply_result = Text()

    def on_multiply_click(e):
        try:
            list1 = list(map(int, list1_field.value.split(',')))
            list2 = list(map(int, list2_field.value.split(',')))
            generator = multiply_arrays_pairs(list1, list2)
            result = [next(generator) for _ in range(min(len(list1), len(list2)))]
            multiply_result.value = f"Результат: {result}"
        except ValueError as ex:
            multiply_result.value = str(ex)
        multiply_result.update()

    multiply_tab_content = Column([
        list1_field, list2_field,
        ElevatedButton("Перемножить пары", on_click=on_multiply_click),
        multiply_result
    ])

    password_length_field = TextField(label="Длина пароля", value="12")
    passwords_count_field = TextField(label="Количество паролей", value="5")
    passwords_result = Text()

    def on_generate_passwords_click(e):
        try:
            length = int(password_length_field.value)
            count = int(passwords_count_field.value)
            passwords = generate_passwords(length, count)
            passwords_result.value = f"Пароли: {', '.join(passwords)}"
        except ValueError as ex:
            passwords_result.value = str(ex)
        passwords_result.update()

    passwords_tab_content = Column([
        password_length_field, passwords_count_field,
        ElevatedButton("Сгенерировать пароли", on_click=on_generate_passwords_click),
        passwords_result
    ])

    tabs = Tabs(
        selected_index=0,
        tabs=[
            Tab(text="Modules", content=modules_tab_content),
            Tab(text="Multiply Pairs", content=multiply_tab_content),
            Tab(text="Passwords", content=passwords_tab_content)
        ]
    )

    page.add(tabs)

ft.app(target=main)
