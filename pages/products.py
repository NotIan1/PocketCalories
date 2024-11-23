import flet as ft

class ChooseProductsPage(ft.View):
    def __init__(self, page):
        super().__init__(route='/choose-products', padding=20)
        self.page = page
        self.page.title = "Choose Products"

        # Title and Search Bar
        self.title = ft.Text("Choose Products", size=24, weight=ft.FontWeight.BOLD)
        self.search_bar = ft.TextField(
            hint_text="Search here...",
            prefix_icon=ft.icons.SEARCH,
            width=300,
            border_radius=8,
        )

        # Add Product Button
        self.add_button = ft.IconButton(
            icon=ft.icons.ADD_CIRCLE,
            icon_size=50,
            tooltip="Add New Product",
            on_click=lambda _: self.page.go("/add-product")  # Navigate to Add Product Page
        )

        # Categories
        self.categories = {
            "Proteins": [
                self.create_product_card("Red Fish", "assets/red_fish.png"),
                self.create_product_card("Meat", "assets/meat.png"),
                self.create_product_card("Eggs", "assets/eggs.png"),
            ],
            "Carbs": [
                self.create_product_card("Pasta", "assets/pasta.png"),
                self.create_product_card("Rice", "assets/rice.png"),
            ],
            "Fats": [
                self.create_product_card("Nuts", "assets/nuts.png"),
            ],
            "Others": []
        }

        # Grid Layout for Categories
        self.controls = [
            ft.Row([self.title, self.search_bar], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(),
            *[
                ft.Column(
                    [
                        ft.Text(category, size=18, weight=ft.FontWeight.BOLD),
                        ft.GridView(
                            max_extent=150,
                            spacing=10,
                            run_spacing=10,
                            controls=self.categories[category]
                        ),
                    ],
                    spacing=10
                )
                for category in self.categories
            ],
            ft.Row([self.add_button], alignment=ft.MainAxisAlignment.END),
        ]

    def create_product_card(self, product_name, image_path):
        """Creates a product card with image, name, and quantity controls."""
        quantity_text = ft.TextField(value="1", width=50, text_align="center", border_radius=8)

        return ft.Container(
            content=ft.Column([
                ft.Image(src=image_path, width=80, height=80, fit=ft.ImageFit.CONTAIN),
                ft.Text(product_name, size=14, weight=ft.FontWeight.BOLD),
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.REMOVE,
                            icon_size=16,
                            on_click=lambda _: self.update_quantity(quantity_text, -1)
                        ),
                        quantity_text,
                        ft.IconButton(
                            icon=ft.icons.ADD,
                            icon_size=16,
                            on_click=lambda _: self.update_quantity(quantity_text, 1)
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
            ]),
            padding=8,
            border_radius=8,
            border=ft.border.all(color=ft.colors.GREY_200),
            bgcolor=ft.colors.WHITE,
            alignment=ft.alignment.center
        )

    def update_quantity(self, quantity_text, delta):
        """Updates the quantity value of a product."""
        try:
            current_quantity = int(quantity_text.value)
            new_quantity = max(1, current_quantity + delta)  # Ensure quantity is at least 1
            quantity_text.value = str(new_quantity)
            self.page.update()
        except ValueError:
            quantity_text.value = "1"
            self.page.update()
