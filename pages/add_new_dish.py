import flet as ft

class AddDishPage(ft.View):
    def __init__(self, page):
        super().__init__(route='/add-dish', padding=20)
        self.page = page
        self.page.title = "Add New Dish"

        # Title and Input Fields
        self.title_text = ft.Text("Add New Dish", size=24, weight=ft.FontWeight.BOLD)
        self.dish_name = ft.TextField(label="Name", width=400, border_radius=8)
        self.description = ft.TextField(label="Description", multiline=True, width=400, border_radius=8)
        self.cooking_time = ft.TextField(label="Time to Make (e.g., 10-15 min)", width=400, border_radius=8)
        self.difficulty = ft.Dropdown(
            label="Difficulty",
            options=[
                ft.dropdown.Option("Easy"),
                ft.dropdown.Option("Medium"),
                ft.dropdown.Option("Hard")
            ],
            width=200
        )
        self.calories = ft.TextField(label="Calories", width=100, border_radius=8)
        self.proteins = ft.TextField(label="Proteins", width=100, border_radius=8)
        self.fats = ft.TextField(label="Fats", width=100, border_radius=8)
        self.carbs = ft.TextField(label="Carbs", width=100, border_radius=8)

        # Image Upload
        self.image_picker = ft.FilePicker(on_result=self.upload_image)
        self.image_display = ft.Image(width=200, height=150, fit=ft.ImageFit.CONTAIN)
        self.image_upload_button = ft.IconButton(
            icon=ft.icons.UPLOAD_FILE,
            tooltip="Upload Image",
            on_click=lambda _: self.page.overlay.append(self.image_picker)
        )

        # Ingredients Section
        self.ingredients_list = ft.ListView(height=200, spacing=10, controls=[])
        self.add_ingredient_button = ft.IconButton(
            icon=ft.icons.ADD_CIRCLE,
            icon_size=50,
            tooltip="Add Ingredient",
            on_click=lambda _: self.page.go("/choose-products")  # Navigate to Choose Product Page
        )

        # Save Button
        self.save_button = ft.ElevatedButton(
            text="Create!",
            bgcolor=ft.colors.GREEN,
            color=ft.colors.WHITE,
            on_click=self.save_dish
        )

        # Layout Arrangement
        self.controls = [
            self.title_text,
            self.dish_name,
            ft.Row([
                ft.Column([self.image_upload_button, self.image_picker], width=220),
                self.image_display
            ]),
            ft.Row([self.description, self.cooking_time]),
            ft.Row([self.difficulty, self.calories]),
            ft.Row([self.proteins, self.fats, self.carbs], spacing=10),
            ft.Text("Ingredients", size=18, weight=ft.FontWeight.BOLD),
            ft.Row([self.add_ingredient_button]),
            self.ingredients_list,
            ft.Row([self.save_button], alignment=ft.MainAxisAlignment.END),
        ]

    def upload_image(self, e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            # Display the uploaded image
            self.image_display.src = f"/uploads/{e.files[0].name}"
            self.page.update()

    def save_dish(self, _):
        # Gather dish information and save it
        new_dish = {
            "name": self.dish_name.value,
            "description": self.description.value,
            "cooking_time": self.cooking_time.value,
            "difficulty": self.difficulty.value,
            "calories": self.calories.value,
            "proteins": self.proteins.value,
            "fats": self.fats.value,
            "carbs": self.carbs.value,
            "ingredients": [
                control.controls[0].value for control in self.ingredients_list.controls
            ],
            "image": self.image_display.src
        }
        print("New Dish Created:", new_dish)
        self.page.go("/")  # Navigate back to main page

    def add_ingredient(self, ingredient):
        """Add ingredient to the list after choosing from the Choose Products Page."""
        ingredient_card = ft.Row([
            ft.Text(ingredient, size=14, weight=ft.FontWeight.BOLD),
            ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda _: self.remove_ingredient(ingredient_card)
            )
        ])
        self.ingredients_list.controls.append(ingredient_card)
        self.page.update()

    def remove_ingredient(self, ingredient_card):
        """Remove an ingredient from the list."""
        self.ingredients_list.controls.remove(ingredient_card)
        self.page.update()
