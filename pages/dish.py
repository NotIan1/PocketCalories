import flet as ft

class DishPage(ft.View):
    def __init__(self, page, dish_name="Pasta with Sausages", dish_info=None):
        super().__init__(route='/dish')
        self.page = page
        self.dish_name = dish_name
        self.dish_info = dish_info or {
            "description": "Time to make: 15-20 mins\nDifficulty: easy\nCalories: 500-600",
            "proteins": "10g",
            "fats": "70g",
            "carbs": "60g",
            "ingredients": [
                {"name": "Pasta", "quantity": "100g", "image": "assets/pasta.png"},
                {"name": "Sausage", "quantity": "100g - 2 sausages", "image": "assets/sausage.png"},
                {"name": "Salt", "quantity": "2 tsp", "image": "assets/salt.png"}
            ]
        }

        # Dish Title
        self.dish_title = ft.Text(self.dish_name, size=24, weight=ft.FontWeight.BOLD)

        # Dish Image with Play Icon Overlay
        self.dish_image = ft.Stack([
            ft.Image(src="assets/dish_image.png", width=200, height=150),
            ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL, icon_size=50, icon_color=ft.colors.RED, on_click=self.play_video)
        ])

        # Dish Description and Nutritional Info
        self.description_text = ft.Text(self.dish_info["description"], size=14)
        self.nutrition_text = ft.Text(
            f"Proteins: {self.dish_info['proteins']}\nFats: {self.dish_info['fats']}\nCarbs: {self.dish_info['carbs']}",
            size=14
        )

        # Ingredients Section
        ingredients_grid = ft.Row(
            controls=[
                self.create_ingredient_card(ingredient["name"], ingredient["quantity"], ingredient["image"])
                for ingredient in self.dish_info["ingredients"]
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # "Cook and Eat" Button
        cook_button = ft.ElevatedButton(
            text="Cook and Eat",
            bgcolor=ft.colors.GREEN,
            color=ft.colors.WHITE,
            on_click=lambda _: print("Cooking started!")
        )

        # Layout Arrangement
        self.controls = [
            ft.AppBar(title=ft.Text(self.dish_name), bgcolor="#16E3AF", color=ft.colors.WHITE, ),
            ft.Text("Dish Window", size=20, weight=ft.FontWeight.BOLD),
            self.dish_title,
            ft.Row([self.dish_image, ft.Column([self.description_text, self.nutrition_text, cook_button], spacing=10)]),
            ft.Text("Ingredients", size=18, weight=ft.FontWeight.BOLD),
            ingredients_grid
        ]

    def create_ingredient_card(self, name, quantity, image_path):
        return ft.Container(
            content=ft.Column([
                ft.Image(src=image_path, width=60, height=60),
                ft.Text(name, size=12),
                ft.Text(quantity, size=10, color=ft.colors.GREY)
            ]),
            padding=5,
            border_radius=8,
            border=ft.border.all(color=ft.colors.GREY_200),
            bgcolor=ft.colors.WHITE,
            alignment=ft.alignment.center
        )

    def play_video(self, _):
        print("Playing video...")
