import flet as ft

from calculations.activity_calculations import calculate_calories
from data.user_params import UserParameters


class MainWindowPage(ft.View):
    def __init__(self, page, navbar):
        super().__init__(route='/', padding=20)
        self.page = page
        self.navbar = navbar
        self.user_params = UserParameters.create(page)

        # Calculate calories based on parameters stored in client_storage
        self.calories_needed = self.calculate_needed_calories()

        # Display calories
        self.calories_text = ft.Text(
            f"Calories needed per day: {self.calories_needed}",
            size=18,
            color=ft.colors.BLACK87
        )

        # Page controls
        self.controls = [
            ft.AppBar(title=ft.Text("Main Window"), bgcolor="#16E3AF", color=ft.colors.WHITE),
            self.navbar,
            self.calories_text  # Add calories information to the display
        ]

    def calculate_needed_calories(self):
        # Calculate and return calories
        return calculate_calories(intensity="average", **self.user_params.to_dict())
