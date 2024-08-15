import flet as ft

def main(page: ft.Page):
    page.title = "Your Parameters"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#E8F0F2"  # Light blue background color

    def increment(text_ref):
        text_ref.value = str(int(text_ref.value) + 1)
        page.update()

    def decrement(text_ref):
        if int(text_ref.value) > 0:
            text_ref.value = str(int(text_ref.value) - 1)
            page.update()

    # Define input fields
    name = ft.TextField(label="What's your name:", width=300)

    age_value = ft.Text("1")
    age = ft.Row([
        ft.IconButton(ft.icons.REMOVE, on_click=lambda _: decrement(age_value), icon_color=ft.colors.RED),
        age_value,
        ft.IconButton(ft.icons.ADD, on_click=lambda _: increment(age_value), icon_color=ft.colors.GREEN),
    ], alignment=ft.MainAxisAlignment.CENTER)

    weight_value = ft.Text("1")
    weight = ft.Row([
        ft.IconButton(ft.icons.REMOVE, on_click=lambda _: decrement(weight_value), icon_color=ft.colors.RED),
        weight_value,
        ft.IconButton(ft.icons.ADD, on_click=lambda _: increment(weight_value), icon_color=ft.colors.GREEN),
    ], alignment=ft.MainAxisAlignment.CENTER)

    height_value = ft.Text("1")
    height = ft.Row([
        ft.IconButton(ft.icons.REMOVE, on_click=lambda _: decrement(height_value), icon_color=ft.colors.RED),
        height_value,
        ft.IconButton(ft.icons.ADD, on_click=lambda _: increment(height_value), icon_color=ft.colors.GREEN),
    ], alignment=ft.MainAxisAlignment.CENTER)

    main_sport = ft.Dropdown(
        label="Main sport:",
        options=[
            ft.dropdown.Option("Swimming"),
            ft.dropdown.Option("Running"),
            ft.dropdown.Option("Cycling"),
            ft.dropdown.Option("Other"),
        ],
        width=300
    )

    training_times_value = ft.Text("1")
    training_times = ft.Row([
        ft.IconButton(ft.icons.REMOVE, on_click=lambda _: decrement(training_times_value), icon_color=ft.colors.RED),
        training_times_value,
        ft.IconButton(ft.icons.ADD, on_click=lambda _: increment(training_times_value), icon_color=ft.colors.GREEN),
    ], alignment=ft.MainAxisAlignment.CENTER)

    allergies = ft.TextField(label="Allergies:", width=300)

    save_button = ft.ElevatedButton("Save", width=300, style=ft.ButtonStyle(
        color=ft.colors.WHITE,
        bgcolor="#00796B",  # Teal color for the button
        shape=ft.RoundedRectangleBorder(radius=10),
        padding={"top": 10, "bottom": 10, "left": 10, "right": 10}
    ))

    # Assemble the page layout
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("Your Parameters:", size=24, weight=ft.FontWeight.BOLD, color="#00796B"),  # Teal color for the title
                ft.Container(height=20),  # Spacer
                name,
                ft.Container(height=20),  # Spacer
                ft.Text("Age:", size=16, color=ft.colors.BLACK87),
                age,
                ft.Container(height=20),  # Spacer
                ft.Text("Weight:", size=16, color=ft.colors.BLACK87),
                weight,
                ft.Container(height=20),  # Spacer
                ft.Text("Height:", size=16, color=ft.colors.BLACK87),
                height,
                ft.Container(height=20),  # Spacer
                main_sport,
                ft.Container(height=20),  # Spacer
                ft.Text("Times a week of training:", size=16, color=ft.colors.BLACK87),
                training_times,
                ft.Container(height=20),  # Spacer
                allergies,
                ft.Container(height=30),  # Spacer
                save_button
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=30,
            border_radius=ft.border_radius.all(20),
            bgcolor=ft.colors.WHITE,
            width=350,
            alignment=ft.alignment.center
        )
    )

ft.app(target=main)
