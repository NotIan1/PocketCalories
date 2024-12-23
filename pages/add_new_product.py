import flet as ft


class AddProductPage(ft.View):
    def __init__(self, page):
        super().__init__(route='/add-product', padding=20)
        self.page = page
        self.page.title = "Add New Product"

        # Input Fields
        self.product_name = ft.TextField(label="Name", width=400, border_radius=8)

        # Image Upload
        self.image_picker = ft.FilePicker(on_result=self.upload_image)
        self.image_display = ft.Image(width=200, height=150, fit=ft.ImageFit.CONTAIN)
        self.image_upload_button = ft.IconButton(
            icon=ft.icons.UPLOAD_FILE,
            tooltip="Upload product image",
            on_click=lambda _: self.page.overlay.append(self.image_picker)
        )

        # Category Dropdown
        self.category_dropdown = ft.Dropdown(
            label="Category",
            width=200,
            options=[
                ft.dropdown.Option("Proteins"),
                ft.dropdown.Option("Carbohydrates"),
                ft.dropdown.Option("Fats"),
                ft.dropdown.Option("Others")
            ]
        )

        # Units Dropdown
        self.units_dropdown = ft.Dropdown(
            label="Units",
            width=200,
            options=[
                ft.dropdown.Option("Pieces"),
                ft.dropdown.Option("Grams"),
                ft.dropdown.Option("Milligrams"),
                ft.dropdown.Option("Liters")
            ]
        )

        # Nutritional Information
        self.carbs = ft.TextField(label="Carbs (g)", width=100, border_radius=8)
        self.protein = ft.TextField(label="Protein (g)", width=100, border_radius=8)
        self.fats = ft.TextField(label="Fats (g)", width=100, border_radius=8)
        self.calories = ft.TextField(label="Calories (kcal)", width=100, border_radius=8)

        # Save Button
        self.save_button = ft.ElevatedButton(
            text="Save Product",
            bgcolor=ft.colors.GREEN,
            color=ft.colors.WHITE,
            on_click=self.save_product
        )

        # Layout Arrangement
        self.controls = [
            ft.AppBar(
                title=ft.Text("Add New Product", color=ft.colors.ON_PRIMARY),
                bgcolor=ft.colors.PRIMARY
            ),
            self.product_name,
            ft.Row([
                ft.Column([self.image_upload_button, self.image_picker], width=220),
                self.image_display
            ]),
            ft.Row([self.category_dropdown, self.units_dropdown], spacing=20),
            ft.Row([self.carbs, self.protein, self.fats, self.calories], spacing=10),
            ft.Row([self.save_button], alignment=ft.MainAxisAlignment.END)
        ]

    def upload_image(self, e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            # Display the uploaded image (assuming it's in an accessible directory)
            self.image_display.src = f"/uploads/{e.files[0].name}"
            self.page.update()

    def save_product(self, _):
        # Gather product information
        new_product = {
            "name": self.product_name.value,
            "category": self.category_dropdown.value,
            "units": self.units_dropdown.value,
            "carbs": self.carbs.value,
            "protein": self.protein.value,
            "fats": self.fats.value,
            "calories": self.calories.value,
            "image": self.image_display.src
        }
        # Example: Print or store the new product details
        # TODO: saving in db
        print("New Product Saved:", new_product)
        self.page.go("/")  # Navigate back to the main page
