import flet as ft

class AddDishPage(ft.View):
    def __init__(self, page):
        super().__init__(route='/add-dish', padding=20)
        self.page = page
        self.page.title = "Add New Dish"

        # Title Text
        self.title_text = ft.Text("Add a New Dish", size=24, weight=ft.FontWeight.BOLD)

        # Input fields
        self.dish_name = ft.TextField(label="Dish Name", width=400, border_radius=8)
        self.calories = ft.TextField(label="Calories (e.g., 500)", width=400, border_radius=8)
        self.cooking_time = ft.TextField(label="Cooking Time (e.g., 15-20 mins)", width=400, border_radius=8)
        self.difficulty = ft.Dropdown(
            label="Difficulty",
            width=400,
            options=[
                ft.dropdown.Option("Easy"),
                ft.dropdown.Option("Medium"),
                ft.dropdown.Option("Hard")
            ]
        )
        self.image_picker = ft.FilePicker(on_result=self.upload_image)
        self.image_display = ft.Image(width=200, height=150, fit=ft.ImageFit.CONTAIN)
        self.image_upload_button = ft.IconButton(
            icon=ft.icons.UPLOAD_FILE,
            on_click=lambda _: self.page.overlay.append(self.image_picker)
        )

        # Ingredients Section
        self.ingredient_name = ft.TextField(label="Ingredient Name", width=200, border_radius=8)
        self.ingredient_quantity = ft.TextField(label="Quantity (e.g., 100g)", width=200, border_radius=8)
        self.ingredients_list = ft.ListView(height=200, spacing=10, controls=[])
        self.add_ingredient_button = ft.ElevatedButton(
            text="Add Ingredient",
            on_click=self.add_ingredient
        )

        # Save Button
        self.save_button = ft.ElevatedButton(
            text="Save Dish",
            bgcolor=ft.colors.GREEN,
            color=ft.colors.WHITE,
            on_click=self.save_dish
        )

        # Layout Arrangement
        self.controls = [
            self.title_text,
            self.dish_name,
            self.calories,
            self.cooking_time,
            self.difficulty,
            ft.Row([
                ft.Column([self.image_upload_button, self.image_picker], width=220),
                self.image_display
            ]),
            ft.Text("Ingredients", size=18, weight=ft.FontWeight.BOLD),
            ft.Row([self.ingredient_name, self.ingredient_quantity, self.add_ingredient_button]),
            self.ingredients_list,
            ft.Row([self.save_button], alignment=ft.MainAxisAlignment.END)
        ]

    def upload_image(self, e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            # Show the uploaded image (assuming it's in the app's accessible directory)
            self.image_display.src = f"/uploads/{e.files[0].name}"
            self.page.update()

    def add_ingredient(self, _):
        # Add the ingredient to the list
        if self.ingredient_name.value and self.ingredient_quantity.value:
            ingredient_item = ft.Row([
                ft.Text(self.ingredient_name.value, size=14, weight=ft.FontWeight.BOLD),
                ft.Text(self.ingredient_quantity.value, size=14, color=ft.colors.GREY),
                ft.IconButton(
                    icon=ft.icons.DELETE,
                    on_click=lambda _: self.remove_ingredient(ingredient_item)
                )
            ])
            self.ingredients_list.controls.append(ingredient_item)
            self.page.update()
            self.ingredient_name.value = ""
            self.ingredient_quantity.value = ""

    def remove_ingredient(self, ingredient_item):
        # Remove the ingredient from the list
        self.ingredients_list.controls.remove(ingredient_item)
        self.page.update()

    def save_dish(self, _):
        # Save dish logic (could be writing to a database or API)
        new_dish = {
            "name": self.dish_name.value,
            "calories": self.calories.value,
            "cooking_time": self.cooking_time.value,
            "difficulty": self.difficulty.value,
            "ingredients": [
                {"name": control.controls[0].value, "quantity": control.controls[1].value}
                for control in self.ingredients_list.controls
            ],
            "image": self.image_display.src
        }
        print("New Dish Saved:", new_dish)
        self.page.go("/")  # Navigate back to the main page
