import flet as ft

class ParameterPage(ft.View):
    def __init__(self, page):
        """Функция инициализации страницы - она выполняется когда создается страница"""
        # self - объект ParamaterPage
        # page - самый главный page

        super().__init__(route='/parameters', padding=20)
        self.page = page

        # Define input fields
        self.name = ft.TextField(label="What's your name:", width=300)

        self.age_value = ft.Text("1")
        self.age = ft.Row([
            ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.age_value), icon_color=ft.colors.RED),
            self.age_value,
            ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.age_value), icon_color=ft.colors.GREEN),
        ], alignment=ft.MainAxisAlignment.CENTER)

        self.weight_value = ft.Text("1")
        self.weight = ft.Row([
            ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.weight_value), icon_color=ft.colors.RED),
            self.weight_value,
            ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.weight_value), icon_color=ft.colors.GREEN),
        ], alignment=ft.MainAxisAlignment.CENTER)

        self.height_value = ft.Text("1")
        self.height = ft.Row([
            ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.height_value), icon_color=ft.colors.RED),
            self.height_value,
            ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.height_value), icon_color=ft.colors.GREEN),
        ], alignment=ft.MainAxisAlignment.CENTER)

        self.main_sport = ft.Dropdown(
            label="Main sport:",
            options=[
                ft.dropdown.Option("Swimming"),
                ft.dropdown.Option("Running"),
                ft.dropdown.Option("Cycling"),
                ft.dropdown.Option("Other"),
            ],
            width=300
        )

        self.training_times_value = ft.Text("1")
        self.training_times = ft.Row([
            ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.training_times_value),
                          icon_color=ft.colors.RED),
            self.training_times_value,
            ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.training_times_value), icon_color=ft.colors.GREEN),
        ], alignment=ft.MainAxisAlignment.CENTER)

        self.allergies = ft.TextField(label="Allergies:", width=300)

        self.save_button = ft.ElevatedButton("Save", width=300,
                                             on_click=lambda _: self.page.go('/'),
                                             style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor="#00796B",  # Teal color for the button
            shape=ft.RoundedRectangleBorder(radius=10),
            padding={"top": 10, "bottom": 10, "left": 10, "right": 10}
        ))

        # Assemble the page layout
        self.controls = [
            ft.Container(
                content=ft.Column([
                    ft.Text("Your Parameters:", size=24, weight=ft.FontWeight.BOLD, color="#00796B"),
                    # Teal color for the title
                    ft.Container(height=20),  # Spacer
                    self.name,
                    ft.Container(height=20),  # Spacer
                    ft.Text("Age:", size=16, color=ft.colors.BLACK87),
                    self.age,
                    ft.Container(height=20),  # Spacer
                    ft.Text("Weight:", size=16, color=ft.colors.BLACK87),
                    self.weight,
                    ft.Container(height=20),  # Spacer
                    ft.Text("Height:", size=16, color=ft.colors.BLACK87),
                    self.height,
                    ft.Container(height=20),  # Spacer
                    self.main_sport,
                    ft.Container(height=20),  # Spacer
                    ft.Text("Times a week of training:", size=16, color=ft.colors.BLACK87),
                    self.training_times,
                    ft.Container(height=20),  # Spacer
                    self.allergies,
                    ft.Container(height=30),  # Spacer
                    self.save_button
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=30,
                border_radius=ft.border_radius.all(20),
                bgcolor=ft.colors.WHITE,
                width=350,
                alignment=ft.alignment.center

            )
        ]

    def increment(self, text_ref):
        text_ref.value = str(int(text_ref.value) + 1)
        self.page.update()

    def decrement(self, text_ref):
        if int(text_ref.value) > 0:
            text_ref.value = str(int(text_ref.value) - 1)
            self.page.update()

def main(page: ft.Page):
    page.title = "Your Parameters"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#E8F0F2"  # Light blue background color

    profile = ParameterPage(page)
    page.views.append(profile)
    page.update()


if __name__ == '__main__':
    ft.app(target=main)
