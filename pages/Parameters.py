import flet as ft

class ParameterPage:
    def __init__(self, page):
        """Initializes the ParameterPage."""
        self.page = page

        # Define input fields
        self.name = ft.TextField(label="What's your name:", width=300, on_change=self.validate_form)

        self.age_value = ft.TextField(value="1", width=60, on_change=self.validate_form, text_align=ft.TextAlign.CENTER)
        self.age = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.age_value), icon_color=ft.colors.RED),
                self.age_value,
                ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.age_value), icon_color=ft.colors.GREEN),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.weight_value = ft.TextField(value="1", width=60, on_change=self.validate_form, text_align=ft.TextAlign.CENTER)
        self.weight = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.weight_value), icon_color=ft.colors.RED),
                self.weight_value,
                ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.weight_value), icon_color=ft.colors.GREEN),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.height_value = ft.TextField(value="1", width=60, on_change=self.validate_form, text_align=ft.TextAlign.CENTER)
        self.height = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.height_value), icon_color=ft.colors.RED),
                self.height_value,
                ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.height_value), icon_color=ft.colors.GREEN),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.training_times_value = ft.TextField(value="1", width=60, on_change=self.validate_form, text_align=ft.TextAlign.CENTER)
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
                ft.dropdown.Option("Cycling"),
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

        self.allergies = ft.TextField(label="Allergies:", width=300, on_change=self.validate_form)  # Required field

        self.save_button = ft.ElevatedButton(
            "Save",
            width=300,
            disabled=True,  # Initially disabled
            on_click=lambda _: self.page.go("/"),
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor="#00796B",  # Teal color for the button
                shape=ft.RoundedRectangleBorder(radius=10),
                padding={"top": 10, "bottom": 10, "left": 10, "right": 10},
            ),
        )

        # Assemble the page layout
        self.content = ft.Container(
            content=ft.Column(
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
                    self.allergies,  # Required field, included in validation
                    ft.Container(height=30),  # Spacer
                    self.save_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Center content vertically
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center content horizontally
            ),
            padding=30,
            border_radius=ft.border_radius.all(20),
            bgcolor=ft.colors.WHITE,
            width=350,
        )

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
                self.allergies.value.strip()  # Included in validation
            ])
        except ValueError:
            is_form_valid = False

        self.save_button.disabled = not is_form_valid
        self.page.update()

def main(page: ft.Page):
    page.title = "Your Parameters"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#E8F0F2"  # Light blue background color

    # Create and center the ParameterPage content
    profile = ParameterPage(page)
    page.add(
        ft.Container(
            content=profile.content,
            alignment=ft.alignment.center,  # Center the content
            expand=True,  # Allow the container to expand to fill the page
        )
    )

    page.update()

if __name__ == "__main__":
    ft.app(target=main)
