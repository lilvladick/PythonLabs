import flet as ft
import logging
from postgre.database_connection import *

product_rows = []
logging.basicConfig(filename='app.log', level=logging.INFO)

def create_input_form(connection):
    logging.info("Input form created")
    categories = ["Электроника", "Недвижимость", "Транспорт", "Другое"]
    title_field = ft.TextField(label="Название объявления", width=300)
    description_field = ft.TextField(label="Описание", width=300)
    price_field = ft.TextField(label="Цена", width=300, multiline=True)
    category_field = ft.Dropdown(
        label="Категория",
        width=300,
        options=[ft.dropdown.Option(text=category) for category in categories]
    )
    seller_contacts = ft.TextField(label="Контакты", width=300)

    def save_button_click(e):
        title = title_field.value
        description = description_field.value
        price = price_field.value

        product_rows.append({
            'title': title,
            'description': description,
            'price': price,
            'category': category_field.value,
            'contacts': seller_contacts.value
        })

        save_data(connection, [title, description, price, category_field.value, seller_contacts.value])
        logging.info("data saved")

        title_field.value = ""
        description_field.value = ""
        price_field.value = ""
        category_field.value = None
        seller_contacts.value = ""

    save_button = ft.ElevatedButton("Save", on_click=save_button_click)

    return ft.Column(
        [
            title_field,
            description_field,
            price_field,
            category_field,
            seller_contacts,
            save_button,
            ft.Text("")
        ]
    )


def create_data_table(connection):
    result = get_data(connection, "SELECT title, description, price, category, seller_contacts FROM products")
    for row in result:
        product_rows.append({
            'title': row[0],
            'description': row[1],
            'price': row[2],
            'category': row[3],
            'contacts': row[4]
        })
    columns = [
        ft.DataColumn(ft.Text("Title")),
        ft.DataColumn(ft.Text("Description")),
        ft.DataColumn(ft.Text("Price"), numeric=True),
        ft.DataColumn(ft.Text("Category")),
        ft.DataColumn(ft.Text("Contacts"))
    ]

    def create_data_row(product):
        return ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(product['title'])),
                ft.DataCell(ft.Text(product['description'])),
                ft.DataCell(ft.Text(str(product['price']))),
                ft.DataCell(ft.Text(product['category'])),
                ft.DataCell(ft.Text(product['contacts']))
            ]
        )

    data_table = ft.DataTable(columns=columns, rows=[create_data_row(product) for product in product_rows])
    logging.info("Table created")
    return data_table



def main(page: ft.Page):
    logging.info("Program started")
    connection = database_connect()
    data_table = create_data_table(connection)

    input_form = create_input_form(connection)

    def update_table(e):
        data_table.rows = [create_data_row(product) for product in product_rows]
        page.update()
        logging.info("Table updated")



    def create_data_row(product):
        logging.info("Table created")
        return ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(product['title'])),
                ft.DataCell(ft.Text(product['description'])),
                ft.DataCell(ft.Text(str(product['price']))),
                ft.DataCell(ft.Text(product['category'])),
                ft.DataCell(ft.Text(product['contacts']))
            ]
        )

    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Актуальные предложения",
                content=ft.Container(
                    content=data_table, alignment=ft.alignment.top_center
                ),
            ),
            ft.Tab(
                text="Создать объявление",
                icon=ft.icons.ADD,
                content=ft.Container(
                    content=input_form, alignment=ft.alignment.top_center
                ),
            ),
        ],
        expand=1,
    )


    page.title = "Доска 24"
    page.horizontal_alignment = "center"
    page.add(t)
    page.add(ft.ElevatedButton("Обновить доску", on_click=lambda e: update_table(e)))

if __name__ == '__main__':
    ft.app(main)