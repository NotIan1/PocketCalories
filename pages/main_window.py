import flet as ft

from calculations.activity_calculations import calculate_calories
from data.user_params import UserParameters


class MainWindowPage(ft.View):
    def __init__(self, page):
        super().__init__(route='/', padding=20)
        self.page = page
        self.user_params = UserParameters.create(page)

        # Calculate calories based on parameters stored in client_storage
        self.calories_needed = self.page.client_storage.get("calories_needed") or 0

        # Display calories
        self.calories_text = ft.Text(
            f"Calories needed per day: {self.calories_needed}",
            size=18,
            color=ft.colors.BLACK87
        )

        # Page controls
        self.controls = [
            ft.AppBar(title=ft.Text("Main Window"), bgcolor="#16E3AF", color=ft.colors.WHITE),
            self.calories_text  # Add calories information to the display
        ]

        self.navigation_bar = self.page.navigation_bar
