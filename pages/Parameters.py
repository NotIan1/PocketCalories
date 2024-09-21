import flet as ft

class ParameterPage(ft.View):
    def __init__(self, page):
        """Initializes the ParameterPage."""
        super().__init__(route='/parameters', padding=20)
        self.page = page

        # Define input fields
        self.name = ft.TextField(label="What's your name:", width=300, on_change=self.validate_form)

        self.age_value = ft.TextField(value="0", width=60, on_change=self.validate_form, text_align=ft.TextAlign.CENTER)
        self.age = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.age_value), icon_color=ft.colors.RED),
                self.age_value,
                ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.age_value), icon_color=ft.colors.GREEN),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.weight_value = ft.TextField(value="0", width=60, on_change=self.validate_form, text_align=ft.TextAlign.CENTER)
        self.weight = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.weight_value), icon_color=ft.colors.RED),
                self.weight_value,
                ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.weight_value), icon_color=ft.colors.GREEN),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.height_value = ft.TextField(value="0", width=60, on_change=self.validate_form, text_align=ft.TextAlign.CENTER)
        self.height = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.height_value), icon_color=ft.colors.RED),
                self.height_value,
                ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.height_value), icon_color=ft.colors.GREEN),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.training_times_value = ft.TextField(value="0", width=60, on_change=self.validate_form, text_align=ft.TextAlign.CENTER)
        self.training_times = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.training_times_value), icon_color=ft.colors.RED),
                self.training_times_value,
                ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.training_times_value), icon_color=ft.colors.GREEN),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.main_sport = ft.Dropdown(
            label="Main sport:",
            options=[
                ft.dropdown.Option("Swimming"),
                ft.dropdown.Option("Running"),
                ft.dropdown.Option("Boxing"),
                ft.dropdown.Option("Hockey"),
                ft.dropdown.Option("Ice Hockey"),
                ft.dropdown.Option("Squash"),
                ft.dropdown.Option("Cycling"),
                ft.dropdown.Option("Tennis"),
                ft.dropdown.Option("Netball"),
                ft.dropdown.Option("Basketball"),
                ft.dropdown.Option("Other"),
            ],
            width=300,
            on_change=self.validate_form
        )

        self.your_goal = ft.Dropdown(
            label="Your Goal:",
            options=[
                ft.dropdown.Option("Cut"),
                ft.dropdown.Option("Bulk"),
                ft.dropdown.Option("Stay the same weight"),
                ft.dropdown.Option("No goals yet"),
            ],
            width=300,
            on_change=self.validate_form
        )

        self.allergies = ft.TextField(label="Allergies: *", width=300, bgcolor=ft.colors.GREY)  # Optional field

        self.save_button = ft.ElevatedButton(
            "Save",
            width=300,
            disabled=True,  # Initially disabled
            on_click=self.submit,
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=ft.colors.RED,  # Teal color for the button

                shape=ft.RoundedRectangleBorder(radius=10),
                padding={"top": 10, "bottom": 10, "left": 10, "right": 10},
            ),
        )

        # Assemble the page layout
        self.controls = [ft.Row(
            controls=[ft.Column(
                [
                    ft.Text("Your Parameters:", size=24, weight=ft.FontWeight.BOLD, color="#00796B"),  # Teal color for the title
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
                    self.your_goal,
                    ft.Container(height=20),
                    ft.Text("Times a week of training:", size=16, color=ft.colors.BLACK87),
                    self.training_times,
                    ft.Container(height=20),  # Spacer
                    self.allergies,
                    ft.Container(height=30),  # Spacer
                    self.save_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Center content vertically
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center content horizontally
            )],
            alignment=ft.MainAxisAlignment.CENTER,
        )]

    def increment(self, text_ref):
        try:
            text_ref.value = str(int(text_ref.value) + 1)
        except ValueError:
            text_ref.value = "1"
        self.validate_form(None)
        self.page.update()

    def decrement(self, text_ref):
        try:
            value = int(text_ref.value)
            if value > 1:
                text_ref.value = str(value - 1)
            else:
                text_ref.value = "1"
        except ValueError:
            text_ref.value = "1"
        self.validate_form(None)
        self.page.update()

    def validate_form(self, e):
        """Enables the Save button only if all required fields are filled, including allergies."""
        try:
            is_form_valid = all([
                self.name.value.strip(),
                int(self.age_value.value) > 0,
                int(self.weight_value.value) > 0,
                int(self.height_value.value) > 0,
                self.main_sport.value,
                self.your_goal.value,
                int(self.training_times_value.value) > 0,
                # self.allergies.value.strip()  # Included in validation
            ])
        except ValueError:
            is_form_valid = False

        self.save_button.disabled = not is_form_valid
        self.save_button.style.bgcolor = (
            "#4CAF50" if is_form_valid else ft.colors.RED
        )  # Change color to green when enabled, red when disabled
        self.page.update()

    def submit(self, e) -> None:
        self.page.client_storage.set("name", self.name.value)
        self.page.client_storage.set("age", int(self.age_value.value))
        self.page.client_storage.set("weight", int(self.weight_value.value))
        self.page.client_storage.set("height", int(self.height_value.value))
        self.page.client_storage.set("mainsport", self.main_sport.value)
        self.page.client_storage.set("goal", self.your_goal.value)
        self.page.client_storage.set("training times", int(self.training_times_value.value))
        self.page.client_storage.set("allergies", self.allergies.value)
        self.page.go("/")


def main(page: ft.Page):
    page.title = "Your Parameters"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#E8F0F2"  # Light blue background color
    page.window_width = 350
    page.window_height = 1080

    # Create and center the ParameterPage content
    parameters = ParameterPage(page)
    page.views.append(parameters)

    page.update()

if __name__ == "__main__":
    ft.app(target=main)
