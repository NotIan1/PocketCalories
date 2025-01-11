import flet as ft

from config import DATABASE_DIR, RECIPES_IMAGES_DIR
from data.user_params import UserParameters
import sqlite3

def get_all_recipes():
    """
    Query the 'recipes' table in the SQLite database and return two lists:
    - main_recipes  (for meals)
    - extra_recipes (for extras)
    """
    conn = sqlite3.connect(DATABASE_DIR)
    c = conn.cursor()

    # Example table schema:
    #   CREATE TABLE recipes (
    #       name TEXT,
    #       calories INTEGER,
    #       image_path TEXT,
    #       is_extra INTEGER
    #   );
    #
    #   is_extra could be 0 (false) or 1 (true)

    c.execute("SELECT name, calories, image FROM Dishes")
    rows = c.fetchall()

    main_recipes = []
    extra_recipes = []

    for name, cal, img_path in rows:
        # Convert DB row to a dict that matches your card creation
        recipe_data = {
            "title": name,
            "calories": f"{cal} cal",   # e.g. "600 cal"
            "image": img_path
        }
        main_recipes.append(recipe_data)

    conn.close()
    return main_recipes, extra_recipes


class MainWindowPage(ft.View):
    def __init__(self, page):
        super().__init__(route='/', padding=20)
        self.page = page

        self.page.update()

        self.user_params = UserParameters.create(page)
        self.navigation_bar = self.page.navigation_bar

        # Calculate calories based on parameters stored in client_storage
        self.calories_needed = self.page.client_storage.get("calories_needed") or 0
        self.calories_eaten = self.page.client_storage.get("calories_eaten") or 0

        # Calories information
        self.calories_text = ft.Text(
            f"Calories today: {self.calories_eaten} / {self.calories_needed}",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.ON_SURFACE
        )
        self.lunchtime_text = ft.Text("Until Lunchtime: 20 mins", size=16, color=ft.colors.ON_SURFACE)

        # Search bar
        self.search_bar = ft.TextField(
            hint_text="Search here...",
            width=200,
            border_radius=8,
            prefix_icon=ft.icons.SEARCH,
            bgcolor=ft.colors.SURFACE_VARIANT,
            color=ft.colors.ON_SURFACE,
            hint_style=ft.TextStyle(color=ft.colors.ON_SURFACE_VARIANT)
        )

        #
        # 1. Fetch recipes from the DB
        #
        main_recipes, extra_recipes = get_all_recipes()

        #
        # 2. Create GridView for main recipes
        #
        meal_items = ft.GridView(
            max_extent=150,  # size of each card
            padding=10,
            spacing=10,
            run_spacing=10,
            controls=[
                self.create_meal_card(r["title"], r["calories"], r["image"])
                for r in main_recipes
            ]
        )

        #
        # 3. Create GridView for extras
        #
        extra_items = ft.GridView(
            max_extent=100,
            padding=10,
            spacing=8,
            run_spacing=8,
            controls=[
                self.create_extra_item(r["title"], r["calories"], r["image"])
                for r in extra_recipes
            ]
        )

        # Add custom dish button
        add_button = ft.IconButton(
            icon=ft.icons.ADD_CIRCLE,
            icon_size=50,
            icon_color=ft.colors.PRIMARY,
            tooltip="Add New Dish",
            on_click=lambda _: self.page.go("/add-dish")  # Navigate to AddDishPage
        )

        # Arrange everything in a Column
        from flet import ScrollMode

        self.controls = [
            ft.AppBar(
                title=ft.Text("Main Window", color=ft.colors.ON_PRIMARY),
                bgcolor="#16E3AF"
            ),
            ft.ListView(
                expand=True,  # Ensure it uses available space and allows scrolling
                controls=[
                    ft.Row([self.calories_text, self.lunchtime_text, self.search_bar]),
                    ft.Text("Eat Now:", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE),
                    meal_items,
                    ft.Text("Extras:", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE),
                    extra_items,
                    ft.Row([add_button], alignment=ft.MainAxisAlignment.END)
                ]
            )
        ]

    def create_meal_card(self, title, calories, image_path):
        """Create a meal card."""
        return ft.Container(
            content=ft.Column([
                ft.Image(src=RECIPES_IMAGES_DIR + image_path, width=100, height=80),
                ft.Text(title, size=14, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE),
                ft.Text(calories, size=12, color=ft.colors.ON_SURFACE_VARIANT),
                ft.IconButton(
                    icon=ft.icons.CANCEL,
                    icon_color=ft.colors.ERROR,
                    icon_size=16,
                    on_click=lambda _: print("Remove item")
                )
            ], alignment=ft.MainAxisAlignment.CENTER),
            padding=8,
            border_radius=8,
            border=ft.border.all(color=ft.colors.OUTLINE),
            bgcolor=ft.colors.SURFACE,
            on_click=lambda e: self.open_dish_page(title)
        )

    def create_extra_item(self, title, calories, image_path):
        """Create an extra item card."""
        return ft.Container(
            content=ft.Column([
                ft.Image(src=image_path, width=80, height=60),
                ft.Text(title, size=12, color=ft.colors.ON_SURFACE),
                ft.Text(calories, size=10, color=ft.colors.ON_SURFACE_VARIANT),
                ft.IconButton(
                    icon=ft.icons.CANCEL,
                    icon_color=ft.colors.ERROR,
                    icon_size=12,
                    on_click=lambda _: print("Remove extra item")
                )
            ], alignment=ft.MainAxisAlignment.CENTER),
            padding=5,
            border_radius=8,
            border=ft.border.all(color=ft.colors.OUTLINE),
            bgcolor=ft.colors.SURFACE
        )

    def open_dish_page(self, dish_name):
        """Navigate to the dish details page."""
        self.page.go(f"/dish?name={dish_name}")
