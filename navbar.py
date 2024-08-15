import flet as ft


def navbar(page):
    def change_page(e, page):
        page_index = e.control.selected_index
        if page_index == 0:
            page.go("/")
        elif page_index == 1:
            page.go("/schedule")
        elif page_index == 2:
            page.go("/profile")

    navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.icons.SCHEDULE, label="Schedule"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Profile",),
        ],
        on_change=lambda e: change_page(e, page)
    )
    return navigation_bar
