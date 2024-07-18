import flet as ft


def main(page: ft.Page):
    page.title = "Your Parameters"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def increment(text_ref):
        text_ref.value = str(int(text_ref.value) + 1)
        page.update()

    def decrement(text_ref):
        if int(text_ref.value) > 0:
            text_ref.value = str(int(text_ref.value) - 1)
            page.update()

    name = ft.TextField(label="What's your name:", width=200)

    age_value = ft.Text("1")
    age = ft.Row([
        ft.IconButton(ft.icons.REMOVE, on_click=lambda _: decrement(age_value)),
        age_value,
        ft.IconButton(ft.icons.ADD, on_click=lambda _: increment(age_value)),
    ], alignment=ft.MainAxisAlignment.CENTER)

    weight_value = ft.Text("1")
    weight = ft.Row([
        ft.IconButton(ft.icons.REMOVE, on_click=lambda _: decrement(weight_value)),
        weight_value,
        ft.IconButton(ft.icons.ADD, on_click=lambda _: increment(weight_value)),
    ], alignment=ft.MainAxisAlignment.CENTER)

    height_value = ft.Text("1")
    height = ft.Row([
        ft.IconButton(ft.icons.REMOVE, on_click=lambda _: decrement(height_value)),
        height_value,
        ft.IconButton(ft.icons.ADD, on_click=lambda _: increment(height_value)),
    ], alignment=ft.MainAxisAlignment.CENTER)

    main_sport = ft.Dropdown(label="Main sport:", options=[
        ft.dropdown.Option("Swimming"),
        ft.dropdown.Option("Running"),
        ft.dropdown.Option("Cycling"),
        ft.dropdown.Option("Other"),
    ])

    training_times_value = ft.Text("1")
    training_times = ft.Row([
        ft.IconButton(ft.icons.REMOVE, on_click=lambda _: decrement(training_times_value)),
        training_times_value,
        ft.IconButton(ft.icons.ADD, on_click=lambda _: increment(training_times_value)),
    ], alignment=ft.MainAxisAlignment.CENTER)

    allergies = ft.TextField(label="Allergies:", width=200)
    save_button = ft.ElevatedButton("Save", width=200)

    page.add(
        ft.Column([
            name,
            ft.Text("Age:"),
            age,
            ft.Text("Weight:"),
            weight,
            ft.Text("Height:"),
            height,
            main_sport,
            ft.Text("Times a week of training:"),
            training_times,
            allergies,
            save_button
        ], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
