import flet as ft

def on_dialog_result(e: ft.FilePickerResultEvent):
    print("Selected files:", e.files)
    print("Selected file or directory:", e.path)

def main(page: ft.Page):
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)

    page.add(
        ft.ElevatedButton("Choose files...",
                          on_click=lambda e: file_picker.pick_files(allow_multiple=True))
    )
    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Title")),
                ft.DataColumn(ft.Text("Description")),
                ft.DataColumn(ft.Text("Price"), numeric=True),
                ft.DataColumn(ft.Text("Category")),
                ft.DataColumn(ft.Text("Contacts")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Jack")),
                        ft.DataCell(ft.Text("Brown")),
                        ft.DataCell(ft.Text("19")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice")),
                        ft.DataCell(ft.Text("Wong")),
                        ft.DataCell(ft.Text("25")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                    ],
                ),
            ],
        ),
    )

if __name__ == '__main__':
    ft.app(main)