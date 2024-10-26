import flet as ft


class MainWindowPage(ft.View):
    def __init__(self, page, navbar):
        super().__init__(route='/', padding=20)
        self.page = page
        self.navbar = navbar

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
        # Retrieve parameter values from client_storage
        age = int(self.page.client_storage.get("age") or 0)
        weight = int(self.page.client_storage.get("weight") or 0)
        height = int(self.page.client_storage.get("height") or 0)
        sport = self.page.client_storage.get("mainsport") or "No Sport"
        intensity = "average"  # Default intensity; replace if available
        goal = (self.page.client_storage.get("goal") or "stay the same").lower()
        gender = (self.page.client_storage.get("gender") or "male").lower()
        sessions_per_week = int(self.page.client_storage.get("training_times") or 0)
        additional_activity = (self.page.client_storage.get("activity_level") or "sedentary").lower()

        # Calculate and return calories
        return calculate_calories(
            age, weight, height, sport, intensity, goal, gender, sessions_per_week, additional_activity
        )
