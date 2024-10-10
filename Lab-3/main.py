import flet as ft
from server import database_connection


def create_input_form():
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
        result_text = ft.Text(f"title: {title}, desc: {description}, price {price}")
        e.control.content.controls.append(result_text)
        e.control.update()

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
    result = database_connection.make_query(connection, "SELECT title, description, price, category, seller_contacts FROM products")
    product_rows = []
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
    return data_table

def main(page: ft.Page):
    connection = database_connection.database_connect()
    data_table = create_data_table(connection)

    input_form = create_input_form()

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

    page.title = "App Title"
    page.horizontal_alignment = "center"
    page.add(t)

if __name__ == '__main__':
    ft.app(main)