import flet as ft

from config import DATABASE_DIR, RECIPES_IMAGES_DIR, WEBSERVER_URL
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


def recommend_meal(calories_left: int, meal_time_label: str, all_recipes: list[dict]) -> dict | None:
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

    # 2) If we found some matches, pick one. For example, pick the highest-calorie meal that still fits,
    #    or the first match, or random – up to you.
    if possible_recipes:
        # Example: pick the one that’s closest to our leftover (descending order by cal)
        possible_recipes.sort(key=lambda r: r["calories"], reverse=True)
        return possible_recipes[0]

    # 3) If no valid meal found (maybe leftover cals < everything), fallback to smallest meal or None
    #    For example, pick the meal with the smallest cal in all_recipes:
    fallback = min(all_recipes, key=lambda r: r["calories"]) if all_recipes else None
    if fallback:
        # If even the smallest meal is bigger than leftover, you might just let the user pick or show a "No meal found" message.
        return fallback if fallback["calories"] <= calories_left else None

    return None


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
            "calories": cal,  # e.g. "600 cal"
            "image": img_path
        }
        main_recipes.append(recipe_data)

    conn.close()
    return main_recipes, extra_recipes

class MainWindowPage(ft.View):
    def __init__(self, page):
        super().__init__(route='/', padding=20)
        self.page = page

        # Example: read how many cals we are allowed & already eaten
        self.calories_needed = page.client_storage.get("calories_needed") or 0
        self.calories_eaten = page.client_storage.get("calories_eaten") or 0
        calories_left = int(self.calories_needed) - int(self.calories_eaten)

        # Fetch or unify your recipes. Adjust as needed:
        main_recipes, extra_recipes = get_all_recipes()
        all_recipes = main_recipes + extra_recipes  # if you want them all in one list

        # Determine the mealtime
        meal_time_label = get_meal_time_label()  # e.g. "Breakfast", "Lunch", "Dinner", or "Snack"

        # Recommend a meal
        chosen_meal = recommend_meal(calories_left, meal_time_label, all_recipes)

        # Now build the UI to display that recommendation
        if chosen_meal:
            meal_name = chosen_meal["title"]
            meal_cals = chosen_meal["calories"]
            text_value = f"{meal_time_label} recommendation: {meal_name} ({meal_cals} cal)"
        else:
            text_value = "No meal found for your leftover calories."

        self.controls = [
            ft.AppBar(
                title=ft.Text("Main Window", color=ft.colors.ON_PRIMARY),
                bgcolor="#16E3AF"
            ),
            ft.Text(f"Calories so far: {self.calories_eaten}/{self.calories_needed}"),
            ft.Text(text_value, size=16),
            # ... your existing layout ...
        ]

        # At the end of the constructor:
        self.page.update()

    def create_meal_card(self, title, calories, image_path):
        """Create a meal card."""
        return ft.Container(
            content=ft.Column([
                ft.Image(src=WEBSERVER_URL + RECIPES_IMAGES_DIR + image_path, width=100, height=80),
                ft.Text(title, size=14, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE),
                ft.Text(calories, size=12, color=ft.colors.ON_SURFACE_VARIANT),
                ft.IconButton(
                    icon=ft.icons.CANCEL,
                    icon_color=ft.colors.ERROR,
                    icon_size=16,
                    on_click=lambda _: print("Remove item")
                )
            ], alignment=ft.MainAxisAlignment.CENTER),
            width=100,
            height=130,  # Increased height to fit wrapped text
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
            width=100,
            height=130,  # Increased height to fit wrapped text
            padding=5,
            border_radius=8,
            border=ft.border.all(color=ft.colors.OUTLINE),
            bgcolor=ft.colors.SURFACE
        )

    def open_dish_page(self, dish_name):
        """Navigate to the dish details page."""
        self.page.go(f"/dish?name={dish_name}")
