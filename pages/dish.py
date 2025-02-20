import sqlite3
import flet as ft

from config import DATABASE_DIR, PRODUCTS_IMAGES_DIR, WEBSERVER_URL, RECIPES_IMAGES_DIR


class DishPage(ft.View):
    def __init__(self, page, dish_name):
        super().__init__(route='/dish')
        self.page = page
        self.dish_name = dish_name

        # Fetch dish and ingredients details
        self.dish_info, self.ingredients = self.fetch_dish_details(dish_name)

        # Dish Title
        self.dish_title = ft.Text(self.dish_name, size=24, weight=ft.FontWeight.BOLD)

        # Dish Image
        self.dish_image = ft.Image(src=WEBSERVER_URL + RECIPES_IMAGES_DIR + self.dish_info["image"], width=200, height=150)

        # Dish Description and Nutritional Info
        self.description_text = ft.Text(self.dish_info["description"], size=14)
        self.nutrition_text = ft.Text(
            f"Calories: {self.dish_info['calories']} kcal\n"
            f"Protein: {self.dish_info['protein']} g\n"
            f"Fat: {self.dish_info['fat']} g\n"
            f"Carbs: {self.dish_info['carbs']} g",
            size=14
        )

        # Ingredients Section as a Grid
        ingredients_grid = ft.GridView(
            max_extent=120,  # Each item will take up to 120px
            spacing=10,
            run_spacing=10,
            controls=[
                self.create_ingredient_card(ingredient)
                for ingredient in self.ingredients
            ]
        )

        # Recipe Section
        recipe_text = ft.Text(self.dish_info["recipe"], size=14, selectable=True)

        # "Cook and Eat" Button
        cook_button = ft.ElevatedButton(
            text="Cook and Eat",
            bgcolor=ft.colors.GREEN,
            color=ft.colors.WHITE,
            on_click=lambda _: print("Cooking started!")
        )

        # Layout Arrangement
        self.controls = [
            ft.AppBar(title=ft.Text(self.dish_name), bgcolor="#16E3AF", color=ft.colors.WHITE),
            self.dish_title,
            ft.Row([self.dish_image, ft.Column([self.description_text, self.nutrition_text, cook_button], spacing=10)]),
            ft.Text("Ingredients", size=18, weight=ft.FontWeight.BOLD),
            ft.Container(  # Scrollable container for ingredients
                content=ingredients_grid,
                height=200,  # Limit height to enable scrolling
                padding=10,
                border=ft.border.all(color=ft.colors.GREY_200),
                border_radius=8,
                bgcolor=ft.colors.SURFACE
            ),
            ft.Text("Recipe", size=18, weight=ft.FontWeight.BOLD),
            recipe_text
        ]

    def fetch_dish_details(self, dish_name):
        conn = sqlite3.connect(DATABASE_DIR)
        cursor = conn.cursor()

        # Fetch dish details
        cursor.execute("SELECT * FROM Dishes WHERE name = ?", (dish_name,))
        dish_row = cursor.fetchone()
        dish_info = {
            "id": dish_row[0],
            "name": dish_row[1],
            "image": dish_row[2],
            "description": dish_row[3],
            "time_to_make": dish_row[4],
            "serves": dish_row[5],
            "difficulty": dish_row[6],
            "recipe": dish_row[7],
            "calories": dish_row[8],
            "protein": dish_row[9],
            "fat": dish_row[10],
            "carbs": dish_row[11],
        }

        # Fetch ingredients
        cursor.execute("""
            SELECT p.name, dp.quantity, p.image
            FROM DishProduct dp
            JOIN Products p ON dp.product_id = p.id
            WHERE dp.dish_id = ?
        """, (dish_info["id"],))
        ingredients = [
            {"name": row[0], "quantity": row[1], "image": row[2]}
            for row in cursor.fetchall()
        ]

        conn.close()
        return dish_info, ingredients

    def create_ingredient_card(self, ingredient):
        return ft.Container(
            content=ft.Column([
                ft.Image(src=WEBSERVER_URL + PRODUCTS_IMAGES_DIR + ingredient["image"], width=80, height=80, fit=ft.ImageFit.CONTAIN),
                ft.Text(ingredient["name"], size=12, text_align=ft.TextAlign.CENTER),
                ft.Text(f"Qty: {ingredient['quantity']}", size=10, color=ft.colors.GREY, text_align=ft.TextAlign.CENTER)
            ], alignment=ft.MainAxisAlignment.CENTER),
            width=100,
            height=130,  # Increased height to fit wrapped text
            padding=5,
            border_radius=8,
            border=ft.border.all(color=ft.colors.GREY_200),
            bgcolor=ft.colors.WHITE,
            alignment=ft.alignment.center
        )
