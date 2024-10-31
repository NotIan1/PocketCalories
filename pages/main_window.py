import flet as ft
from data.user_params import UserParameters

class MainWindowPage(ft.View):
    def __init__(self, page):
        super().__init__(route='/', padding=20)
        self.page = page
        self.user_params = UserParameters.create(page)
        self.navigation_bar = self.page.navigation_bar

        # Calculate calories based on parameters stored in client_storage
        self.calories_needed = self.page.client_storage.get("calories_needed") or 0
        self.calories_eaten = self.page.client_storage.get("calories_eaten") or 0

        # Calories information
        self.calories_text = ft.Text(
            f"Calories today: {self.calories_eaten} / {self.calories_needed}",
            size=20, weight=ft.FontWeight.BOLD
        )
        self.lunchtime_text = ft.Text("Until Lunchtime: 20 mins", size=16)

        # Search bar
        self.search_bar = ft.TextField(
            hint_text="Search here...",
            width=200,
            border_radius=8,
            prefix_icon=ft.icons.SEARCH,
        )

        # Placeholder for meal images in a grid layout with click event handlers
        meal_items = ft.GridView(
            max_extent=150,  # size of each card
            padding=10,
            spacing=10,
            run_spacing=10,
            controls=[
                self.create_meal_card("Pasta with sausages", "600 cal", "assets/pasta.png"),
                self.create_meal_card("Buckwheat with bacon", "500 cal", "assets/buckwheat.png"),
                self.create_meal_card("Rice with fish", "550 cal", "assets/rice.png"),
            ]
        )

        # Extra meals section
        extra_items = ft.GridView(
            max_extent=100,
            padding=10,
            spacing=8,
            run_spacing=8,
            controls=[
                self.create_extra_item("Carrots", "100 cal", "assets/carrots.png"),
                self.create_extra_item("Protein bar", "200 cal", "assets/protein_bar.png"),
                self.create_extra_item("Apples", "150 cal", "assets/apples.png"),
            ]
        )

        # Add custom dish button
        add_button = ft.IconButton(
            icon=ft.icons.ADD_CIRCLE,
            icon_size=50,
            on_click=lambda _: print("Add custom dish clicked")
        )

        # Arrange everything in a Column
        self.controls = [
            ft.AppBar(title=ft.Text("Main Window"), bgcolor="#16E3AF", color=ft.colors.WHITE, ),
            ft.Row([self.calories_text, self.lunchtime_text, self.search_bar]),
            ft.Text("Eat Now:", size=18, weight=ft.FontWeight.BOLD),
            meal_items,
            ft.Text("Extras:", size=18, weight=ft.FontWeight.BOLD),
            extra_items,
            ft.Row([add_button], alignment=ft.MainAxisAlignment.END)
        ]

    def create_meal_card(self, title, calories, image_path):
        # Each meal card has a click event to navigate to DishPage
        return ft.Container(
            content=ft.Column([
                ft.Image(src=image_path, width=100, height=80),
                ft.Text(title, size=14, weight=ft.FontWeight.BOLD),
                ft.Text(calories, size=12, color=ft.colors.GREY),
                ft.IconButton(icon=ft.icons.CANCEL, icon_size=16, on_click=lambda _: print("Remove item"))
            ]),
            padding=8,
            border_radius=8,
            border=ft.border.all(color=ft.colors.GREY_200),
            bgcolor=ft.colors.WHITE,
            on_click=lambda e: self.open_dish_page(title)  # navigate on click
        )

    def create_extra_item(self, title, calories, image_path):
        return ft.Container(
            content=ft.Column([
                ft.Image(src=image_path, width=80, height=60),
                ft.Text(title, size=12),
                ft.Text(calories, size=10, color=ft.colors.GREY),
                ft.IconButton(icon=ft.icons.CANCEL, icon_size=12, on_click=lambda _: print("Remove extra item"))
            ]),
            padding=5,
            border_radius=8,
            border=ft.border.all(color=ft.colors.GREY_200),
            bgcolor=ft.colors.WHITE
        )

    def open_dish_page(self, dish_name):
        # Push the DishPage to the navigation stack with the dish name
        self.page.go(f'/dish?name={dish_name}')
