import flet as ft

from config import WEBSERVER_URL
from data.user_params import UserParameters
from navbar import navbar

from pages.add_new_dish import AddDishPage
from pages.add_new_product import AddProductPage
from pages.dish import DishPage
from pages.parameters import ParameterPage
from pages.products import ChooseProductsPage
from pages.profile import ProfilePage
from pages.schedule import SchedulePage
from pages.main_window import MainWindowPage
from pages.sign_up import SignupPage

def main(page: ft.Page):
    """
    Main entry point for Pocket Calories,
    with light/dark mode toggling and the SAME teal color (#16E3AF)
    for the top bar in both modes.
    """

    page.title = "Pocket Calories: Same Top Color"

    # -- Our consistent teal color:
    TEAL = "#16E3AF"

    # ------------------------------------------------------------------------
    # 1) Define LIGHT color scheme (with teal for the top bar)
    # ------------------------------------------------------------------------
    light_color_scheme = ft.ColorScheme(
        primary=TEAL,                  # teal for top bar
        on_primary="#FFFFFF",          # white text on teal
        primary_container=TEAL,        # also teal
        on_primary_container="#FFFFFF",

        secondary=TEAL,
        on_secondary="#003B2F",
        secondary_container=TEAL,
        on_secondary_container="#003B2F",

        # Lighter backgrounds for Light Mode
        background="#F7F7F7",
        on_background="#222222",
        surface="#FFFFFF",
        on_surface="#222222",

        surface_variant="#EEEEEE",
        on_surface_variant="#333333",

        outline=TEAL,
        error="#BA1A1A",
        on_error="#FFFFFF"
    )

    # ------------------------------------------------------------------------
    # 2) Define DARK color scheme (with teal for the top bar)
    # ------------------------------------------------------------------------
    dark_color_scheme = ft.ColorScheme(
        primary=TEAL,                  # teal for top bar
        # If you prefer white text on teal in dark mode too, set on_primary="#FFFFFF"
        on_primary="#FFFFFF",
        primary_container=TEAL,
        on_primary_container="#FFFFFF",

        secondary=TEAL,
        on_secondary="#003B2F",
        secondary_container=TEAL,
        on_secondary_container="#003B2F",

        # Dark backgrounds for Dark Mode
        background="#121212",
        on_background="#E1E1E1",
        surface="#1E1E1E",
        on_surface="#EAEAEA",

        surface_variant="#2A2A2A",
        on_surface_variant="#CACACA",

        outline=TEAL,
        error="#CF6679",
        on_error="#000000"
    )

    # ------------------------------------------------------------------------
    # 3) Attach these color schemes to page.light_theme and page.dark_theme
    # ------------------------------------------------------------------------
    page.light_theme = ft.Theme(color_scheme=light_color_scheme, use_material3=True)
    page.dark_theme  = ft.Theme(color_scheme=dark_color_scheme,  use_material3=True)
    page.theme_mode  = ft.ThemeMode.LIGHT   # or DARK, or SYSTEM
    page.adaptive    = True

    # Create the navigation bar
    navigation_bar = navbar(page)
    page.navigation_bar = navigation_bar

    # 4) Toggle button (light <-> dark)
    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    # Put the toggle button in an overlay or your layout
    toggle_btn = ft.IconButton(
        icon=ft.icons.DARK_MODE,
        tooltip="Toggle Light/Dark Mode",
        on_click=toggle_theme
    )
    page.overlay.append(toggle_btn)

    # ------------------------------------------------------------------------
    # 5) Route logic
    # ------------------------------------------------------------------------
    def route_change(route: str):
        troute = page.route
        if troute == '/':
            page.views.clear()
            navigation_bar.selected_index = 0
            page.views.append(MainWindowPage(page))
        elif troute == "/signup":
            page.views.append(SignupPage(page))
        elif troute == "/parameters":
            page.views.append(ParameterPage(page))
        elif troute == "/schedule":
            navigation_bar.selected_index = 1
            page.views.append(SchedulePage(page))
        elif troute == "/profile":
            navigation_bar.selected_index = 2
            page.views.append(ProfilePage(page))
        elif troute.startswith('/dish'):
            dish_name = troute.split("=")[1] if "=" in troute else "Dish"
            page.views.append(DishPage(page, dish_name=dish_name))
        elif troute == '/add-dish':
            page.views.append(AddDishPage(page))
        elif troute == '/add-product':
            page.views.append(AddProductPage(page))
        elif troute == '/choose-products':
            page.views.append(ChooseProductsPage(page))

        page.update()

    def view_pop(view: ft.View):
        page.views.pop()
        top_view = page.views.pop()
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # 6) Check user status
    if not page.client_storage.get('username'):
        page.go('/signup')
    elif not UserParameters.create(page):
        page.go('/parameters')
    else:
        page.go('/')


ft.app(target=main, assets_dir=WEBSERVER_URL)
