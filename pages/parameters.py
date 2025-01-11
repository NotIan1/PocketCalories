import flet as ft

from calculations.activity_calculations import calculate_calories
from data.user_params import UserParameters, Goal, Gender, ActivityLevel
from widgets.sport_selector import SportSelector


class ParameterPage(ft.View):
    def __init__(self, page):
        """Initializes the ParameterPage."""
        super().__init__(route='/parameters', padding=20)
        self.page = page
        self.user_params = UserParameters.create(page)

        # Define input fields (keeping the existing fields, just adjusted for compactness)
        self.name = ft.TextField(label="Name:", value=self.user_params.name,
                                 width=300, on_change=self.validate_form)

        self.gender = ft.Dropdown(
            label="Gender:",
            value=self.user_params.gender.value,
            options=[ft.dropdown.Option(gender.value) for gender in Gender],
            width=300,
            on_change=self.validate_form
        )

        self.age_value = ft.TextField(value=str(self.user_params.age),
                                      width=60, on_change=self.validate_form,
                                      text_align=ft.TextAlign.CENTER)
        self.age = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.age_value),
                              icon_color=ft.colors.RED),
                self.age_value,
                ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.age_value),
                              icon_color=ft.colors.GREEN),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.weight_value = ft.TextField(value=str(self.user_params.weight), width=60,
                                         on_change=self.validate_form,
                                         text_align=ft.TextAlign.CENTER)
        self.weight = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.weight_value),
                              icon_color=ft.colors.RED),
                self.weight_value,
                ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.weight_value),
                              icon_color=ft.colors.GREEN),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.height_value = ft.TextField(value=str(self.user_params.height), width=60,
                                         on_change=self.validate_form,
                                         text_align=ft.TextAlign.CENTER)
        self.height = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.height_value),
                              icon_color=ft.colors.RED),
                self.height_value,
                ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.height_value),
                              icon_color=ft.colors.GREEN),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.training_times_value = ft.TextField(value=str(self.user_params.training_times),
                                                 width=60, on_change=self.validate_form,
                                                 text_align=ft.TextAlign.CENTER)
        self.training_times = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=lambda _: self.decrement(self.training_times_value),
                              icon_color=ft.colors.RED),
                self.training_times_value,
                ft.IconButton(ft.icons.ADD, on_click=lambda _: self.increment(self.training_times_value),
                              icon_color=ft.colors.GREEN),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.main_sport = SportSelector(value=str(self.user_params.main_sport or ""))

        self.your_goal = ft.Dropdown(
            label="Your Goal:",
            value=self.user_params.goal,
            options=[ft.dropdown.Option(goal) for goal in Goal],
            width=300,
            on_change=self.validate_form
        )

        # Activity Level Dropdown
        self.activity_level = ft.Dropdown(
            label="Activity Level:",
            value=self.user_params.activity_level.value,
            options=[ft.dropdown.Option(activity.value) for activity in ActivityLevel],
            width=300,
            on_change=self.validate_form
        )

        # Optional field
        self.allergies = ft.TextField(label="Allergies: *",
                                      value=', '.join(self.user_params.allergies),
                                      width=300, bgcolor=ft.colors.GREY)

        self.save_button = ft.ElevatedButton(
            "Save",
            width=300,
            disabled=True,
            on_click=self.submit,
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=ft.colors.RED,
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=10,
            ),
        )

        self.scroll = ft.ScrollMode.ALWAYS

        # Assemble the page layout
        self.controls = [ft.AppBar(title=ft.Text("Parameters"), bgcolor="#16E3AF", color=ft.colors.WHITE),
                         ft.Column(
                             [
                                 ft.Text("Your Parameters:", size=24, weight=ft.FontWeight.BOLD, color="#00796B"),
                                 # Teal color for the title
                                 ft.Container(height=10),  # Spacer
                                 self.name,
                                 ft.Container(height=10),
                                 self.gender,
                                 ft.Container(height=10),  # Spacer
                                 ft.Text("Age:", size=16, color=ft.colors.BLACK87),
                                 self.age,
                                 ft.Container(height=10),  # Spacer
                                 ft.Text("Weight,kg:", size=16, color=ft.colors.BLACK87),
                                 self.weight,
                                 ft.Container(height=10),  # Spacer
                                 ft.Text("Height,cm:", size=16, color=ft.colors.BLACK87),
                                 self.height,
                                 ft.Container(height=10),  # Spacer
                                 ft.Text("Main sport:", size=16, color=ft.colors.BLACK87),
                                 self.main_sport,
                                 ft.Container(height=10),  # Spacer
                                 self.your_goal,
                                 ft.Container(height=10),
                                 ft.Text("Times a week of training:", size=16, color=ft.colors.BLACK87),
                                 self.training_times,
                                 ft.Container(height=10),
                                 self.activity_level,
                                 ft.Container(height=10),  # Spacer
                                 self.allergies,
                                 ft.Container(height=30),  # Spacer
                                 self.save_button,
                             ],
                             alignment=ft.MainAxisAlignment.CENTER,  # Center content vertically
                             horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center content horizontally
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
        self.user_params.name = self.name.value
        self.user_params.age = int(self.age_value.value)
        self.user_params.weight = int(self.weight_value.value)
        self.user_params.height = int(self.height_value.value)
        self.user_params.main_sport = self.main_sport.sport
        self.user_params.goal = self.your_goal.value
        self.user_params.training_times = int(self.training_times_value.value)
        self.user_params.allergies = [allergy.strip() for allergy in self.allergies.value.split(",")]

        self.page.client_storage.set("calories_needed", calculate_calories(intensity="average", **self.user_params.to_dict()))

        self.page.go("/")


def main(page: ft.Page):
    page.title = "Your Parameters"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#E8F0F2"  # Light blue background color
    page.window.width = 350
    page.window.height = 800

    # Create and center the ParameterPage content
    parameters = ParameterPage(page)
    page.views.append(parameters)

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
