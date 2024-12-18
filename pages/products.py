import flet as ft
import sqlite3

class ChooseProductsPage(ft.View):
    def __init__(self, page):
        super().__init__(route='/choose-products', padding=20)
        self.page = page
        self.page.title = "Choose Products"
        self.page.theme_mode = ft.ThemeMode.DARK  # Enable dark mode
        self.page.update()

        # Title and Search Bar
        self.title = ft.Text("Choose Products", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE)
        self.search_bar = ft.TextField(
            hint_text="Search here...",
            prefix_icon=ft.icons.SEARCH,
            width=300,
            border_radius=8,
            bgcolor=ft.colors.SURFACE_VARIANT,
            color=ft.colors.ON_SURFACE,
            hint_style=ft.TextStyle(color=ft.colors.ON_SURFACE_VARIANT),
            on_change=self.filter_products
        )

        # Add Product Button
        self.add_button = ft.IconButton(
            icon=ft.icons.ADD_CIRCLE,
            icon_size=50,
            tooltip="Add New Product",
            icon_color=ft.colors.PRIMARY,
            on_click=lambda _: self.page.go("/add-product")  # Navigate to Add Product Page
        )

        # Load products from database
        self.categories = self.load_products_from_database()

        # Controls for categories
        self.category_controls = [
            ft.Column(
                [
                    ft.Text(category, size=20, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE),
                    ft.GridView(
                        max_extent=180,
                        spacing=15,
                        run_spacing=15,
                        controls=self.categories[category],
                    ),
                ],
                spacing=10
            )
            for category in self.categories
        ]

        # Create a scrollable layout
        self.controls = [
            ft.ListView(
                controls=[
                    ft.Row([self.title, self.search_bar], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Divider(color=ft.colors.OUTLINE),
                    *self.category_controls,
                    ft.Row([self.add_button], alignment=ft.MainAxisAlignment.END),
                ],
                expand=True,  # Ensures the scrollable area expands to fit available space
                spacing=15
            )
        ]

    def create_product_card(self, product_name, image_path):
        """Creates a product card with image, name, and quantity controls."""
        quantity_text = ft.TextField(
            value="1", width=60, text_align=ft.TextAlign.CENTER,
            border_radius=8, bgcolor=ft.colors.SURFACE_VARIANT, color=ft.colors.ON_SURFACE
        )

        return ft.Container(
            content=ft.Column([
                ft.Image(
                    src='assets/products/' + image_path if image_path else "assets/products/default.png",
                    width=120, height=120, fit=ft.ImageFit.CONTAIN
                ),
                ft.Text(
                    product_name, size=16, weight=ft.FontWeight.BOLD,
                    color=ft.colors.ON_SURFACE, text_align=ft.TextAlign.CENTER
                ),
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.REMOVE,
                            icon_size=20,
                            icon_color=ft.colors.PRIMARY,
                            on_click=lambda _: self.update_quantity(quantity_text, -1)
                        ),
                        quantity_text,
                        ft.IconButton(
                            icon=ft.icons.ADD,
                            icon_size=20,
                            icon_color=ft.colors.PRIMARY,
                            on_click=lambda _: self.update_quantity(quantity_text, 1)
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=8),
            padding=10,
            border_radius=10,
            border=ft.border.all(color=ft.colors.OUTLINE),
            bgcolor=ft.colors.SURFACE,
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

    def load_products_from_database(self):
        """Load product data from the database and categorize it."""
        connection = sqlite3.connect("database/recipe_database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT name, category, image FROM products")
        database_products = cursor.fetchall()

        # Organize products into categories
        categories = {}
        for name, category, image in database_products:
            if category not in categories:
                categories[category] = []
            categories[category].append(
                self.create_product_card(name, image)
            )
        connection.close()
        return categories

    def filter_products(self, e):
        """Filter products based on the search bar input."""
        query = e.control.value.lower()
        for category in self.categories:
            filtered_products = [
                card for card in self.categories[category]
                if query in card.content.controls[1].value.lower()  # Check product name
            ]
            self.categories[category] = filtered_products  # Update category controls
        self.page.update()

