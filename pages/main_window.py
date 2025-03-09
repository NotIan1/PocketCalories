import flet as ft

from config import DATABASE_DIR, RECIPES_IMAGES_DIR, WEBSERVER_URL, PRODUCTS_IMAGES_DIR
from data.user_params import UserParameters
import sqlite3

import datetime


def get_meal_time_label() -> str:
    """Return which meal slot is relevant right now based on the system time."""
    hour = datetime.datetime.now().hour
    if 6 <= hour < 11:
        return "Breakfast"
    elif 11 <= hour < 16:
        return "Lunch"
    elif 16 <= hour < 22:
        return "Dinner"
    else:
        return "Snack"  # e.g. overnight or super-early morning


def recommend_meal(calories_left: int, meal_time_label: str, all_recipes: list[dict]) -> list:
    """
    Chooses one recipe that fits the current meal time *and* doesn't exceed the leftover calories (if possible).

    :param calories_left: How many calories remain for the day (int).
    :param meal_time_label: "Breakfast", "Lunch", "Dinner", or "Snack".
    :param all_recipes: A list of your recipe dicts (with keys like "title", "calories", "meal_type", etc.).
    :return: A single chosen recipe dict or None if nothing fits.
    """

    # 1) Filter recipes by mealtime type if you have meal categories (optional).
    #    If your DB doesn't track "breakfast" vs. "lunch," you can skip or do any filtering you like.
    possible_recipes = []
    if meal_time_label == "Breakfast":
        # E.g., pick recipes labeled "Light" or "Medium" or specifically flagged as breakfast. Adjust logic as needed.
        possible_recipes = [r for r in all_recipes if r["calories"] <= calories_left and r["calories"] <= 500]
    elif meal_time_label == "Lunch":
        possible_recipes = [r for r in all_recipes if r["calories"] <= calories_left and 400 <= r["calories"] <= 700]
    elif meal_time_label == "Dinner":
        possible_recipes = [r for r in all_recipes if r["calories"] <= calories_left and r["calories"] >= 500]
    else:  # "Snack"
        # If it’s late or user only has a small leftover budget, pick a small (<300 cal) recipe
        possible_recipes = [r for r in all_recipes if r["calories"] <= min(calories_left, 300)]

    return possible_recipes



def get_all_recipes():
    """
    Queries your SQLite database and returns:
      - main_recipes (for meals, pulled from the Dishes table)
      - extra_recipes (snackable items, pulled from the Products table)
    """
    conn = sqlite3.connect(DATABASE_DIR)
    c = conn.cursor()

    # 1) Load from the Dishes table
    c.execute("SELECT name, calories, image FROM Dishes")
    rows = c.fetchall()

    main_recipes = []
    for (name, cal, img_path) in rows:
        recipe_data = {
            "title": name,
            "calories": cal,
            "image": img_path
        }
        main_recipes.append(recipe_data)

    # 2) Load snackable products as 'extras'
    c.execute("SELECT name, calories, image FROM Products WHERE snackable = 1")
    product_rows = c.fetchall()

    extra_recipes = []
    for (name, cal, img_path) in product_rows:
        extra_data = {
            "title": name,
            "calories": cal,
            "image": img_path
        }
        extra_recipes.append(extra_data)

    conn.close()
    return main_recipes, extra_recipes

class MainWindowPage(ft.View):
    def __init__(self, page):
        super().__init__(route='/', padding=20)
        self.page = page

        self.user_params = UserParameters.create(page)
        self.navigation_bar = self.page.navigation_bar

        # Calculate calories based on parameters stored in client_storage
        self.calories_needed = self.page.client_storage.get("calories_needed") or 0
        import datetime

        # Retrieve the last recorded date from storage
        last_recorded_date = self.page.client_storage.get("last_recorded_date")
        current_date = datetime.date.today().isoformat()

        # Check if the stored date is different from today's date
        if last_recorded_date != current_date:
            self.page.client_storage.set("calories_eaten", 0)  # Reset calories
            self.page.client_storage.set("last_recorded_date", current_date)  # Update last recorded date

        self.calories_eaten = self.page.client_storage.get("calories_eaten") or 0

        calories_left = int(self.calories_needed) - int(self.calories_eaten)

        # Fetch or unify your recipes. Adjust as needed:
        main_recipes, extra_recipes = get_all_recipes()
        all_recipes = main_recipes  # if you want them all in one list

        # Determine the mealtime
        meal_time_label = get_meal_time_label()  # e.g. "Breakfast", "Lunch", "Dinner", or "Snack"

        # Recommend a meal
        chosen_meals = recommend_meal(calories_left, meal_time_label, all_recipes)
        print(chosen_meals)

        # Calories information
        self.calories_text = ft.Text(
            f"Calories today: {self.calories_eaten} / {self.calories_needed} ({calories_left} left)",
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
        # 2. Create GridView for main recipes
        #
        # In your MainWindowPage __init__ method, update the GridView:
        meal_items = ft.GridView(
            max_extent=350,  # increased to allow a larger card size
            padding=10,
            spacing=10,
            run_spacing=10,
            controls=[
                self.create_meal_card(r["title"], r["calories"], r["image"])
                for r in chosen_meals
            ]
        )

        #
        # 3. Create GridView for extras
        #
        extra_items = ft.GridView(
            max_extent=200,
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
                title=ft.Text("Main Window"),
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


    def eat_now(self, cals: int):
        """Update daily calorie count when user clicks Eat Now."""
        self.calories_eaten += cals
        # Save back to client storage so it persists
        self.page.client_storage.set("calories_eaten", self.calories_eaten)

        cal_left = self.calories_needed - self.calories_eaten
        self.calories_text.value = f"Calories today: {self.calories_eaten} / {self.calories_needed} ({cal_left} left)"
        self.page.update()

    def create_meal_card(self, title, calories, image_path):
        return ft.Container(
            width=350,
            height=450,
            border_radius=30,
            bgcolor=ft.colors.SURFACE,
            border=ft.border.all(color=ft.colors.OUTLINE, width=2),
            padding=16,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    # Smaller Image section
                    ft.Container(
                        content=ft.Image(
                            src=WEBSERVER_URL + RECIPES_IMAGES_DIR + image_path,
                            fit=ft.ImageFit.COVER,
                        ),
                        width=350,
                        height=150,  # Smaller image height
                        border_radius=ft.border_radius.all(20),
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    ),
                    # Text section with title and larger calorie text
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=8,
                        controls=[
                            ft.Text(
                                title,
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.colors.ON_SURFACE
                            ),
                            ft.Text(
                                f"{calories} cal",
                                size=20,  # Increased calorie text size
                                color=ft.colors.ON_SURFACE_VARIANT,
                                text_align=ft.TextAlign.CENTER
                            ),
                        ]
                    ),
                    # "EAT NOW" button that stretches across the whole card with centered content
                    ft.Container(
                        width=350 - 32,  # Adjust for container padding: 350 - (16*2)
                        content=ft.ElevatedButton(
                            # Use content property to create custom layout
                            content=ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.ADD),
                                    ft.Text("EAT NOW", text_align=ft.TextAlign.CENTER)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=10,
                            ),
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.PRIMARY,
                                color=ft.colors.ON_PRIMARY,
                                shape=ft.RoundedRectangleBorder(radius=8),
                                padding=ft.Padding(14, 14, 14, 14)
                            ),
                            on_click=lambda e: self.eat_now(calories),
                        ),
                    ),
                ]
            ),
            on_click=lambda e: self.open_dish_page(title)
        )

    def create_extra_item(self, title, calories, image_path):
        """Create a larger extra card with bigger pictures and text."""
        return ft.Container(
            width=220,  # Increased width
            height=280,  # Increased height
            padding=8,
            border_radius=8,
            border=ft.border.all(color=ft.colors.OUTLINE),
            bgcolor=ft.colors.SURFACE,
            content=ft.Column(
                [
                    ft.Image(
                        src=WEBSERVER_URL + PRODUCTS_IMAGES_DIR + image_path,
                        width=100,  # Increased image width
                        height=70,  # Increased image height
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.Text(
                        title,
                        size=16,  # Increased title text size
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.ON_SURFACE,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        f"{calories} cal",
                        size=14,  # Increased calorie text size
                        color=ft.colors.ON_SURFACE_VARIANT,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                text="Eat Now",
                                icon=ft.icons.ADD,
                                on_click=lambda e: self.eat_now(calories),
                            ),
                            ft.IconButton(
                                icon=ft.icons.CANCEL,
                                icon_color=ft.colors.ERROR,
                                icon_size=16,
                                on_click=lambda _: print("Remove extra item")
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )

    def open_dish_page(self, dish_name):
        """Navigate to the dish details page."""
        self.page.go(f"/dish?name={dish_name}")
