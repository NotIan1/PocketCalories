from typing import Callable

import flet as ft

from data.sports import SPORTS, Sport


from typing import Callable
import flet as ft
from data.sports import SPORTS, Sport

class SportSelector(ft.Container):
    def __init__(
            self,
            page: ft.Page,
            value: str = "",
            intensities=None,
            on_change: Callable[[str], None] | None = None,
            on_add_new_sport: Callable[[str, dict], None] | None = None  # Not used in dropdown version
    ):
        self.page = page
        if intensities is None:
            intensities = {}
        # If a valid sport is provided, use it; otherwise default to the first available sport.
        if value in SPORTS:
            self.value = value
            self.intensities = intensities or SPORTS[value]
        else:
            self.value = next(iter(SPORTS))
            self.intensities = SPORTS[self.value]
        self.on_change = on_change

        # Create a dropdown containing all the sports
        self.dropdown = ft.Dropdown(
            label="Select Sport",
            value=self.value,
            options=[ft.dropdown.Option(sport) for sport in SPORTS.keys()],
            width=300,
            on_change=self.handle_change
        )

        super().__init__(
            content=self.dropdown,
            width=300,
            padding=5,
            bgcolor=ft.colors.GREY_200,
            border_radius=ft.border_radius.all(5)
        )

    @property
    def sport(self):
        # Returns a Sport object with the selected value and its intensities.
        return Sport(self.value, self.intensities)

    def handle_change(self, e):
        self.value = self.dropdown.value
        self.intensities = SPORTS.get(self.value, {})
        if self.on_change:
            self.on_change(self.value)
        self.page.update()


    def set_icon_button(self):
        self.icon_button.current.icon = ft.icons.EDIT if self.value else ft.icons.ADD

    def show_sport_dialog(self):
        # Создаем диалог выбора спорта
        self.sport_dialog = ft.AlertDialog(
            title=ft.Text("Choose Sport"),
            content=ft.Column(
                controls=[
                    ft.TextField(
                        ref=self.search_field,
                        hint_text="Start writing the name of your sport...",
                        on_change=self.filter_sports,
                        autofocus=True
                    ),
                    ft.ListView(
                        ref=self.filtered_list,
                        height=200,
                        spacing=2
                    )
                ],
                tight=True
            ),
            actions=[
                ft.TextButton("Close", on_click=self.close_dialog),
                ft.TextButton("Change", on_click=self.apply_sport_change),
            ]
        )

        # Показываем диалог
        self.page.dialog = self.sport_dialog
        self.sport_dialog.open = True
        self.page.update()

    def show_add_sport_dialog(self, sport_name: str):
        self.add_sport_dialog = ft.AlertDialog(
            title=ft.Text("Add new sport"),
            content=ft.Container(
                width=400,  # Фиксированная ширина диалога
                content=ft.Column(
                    controls=[
                        ft.TextField(
                            ref=self.add_sport_name_field,
                            label="Name of sport",
                            value=sport_name,
                            on_change=self.validate_name,
                            width=400
                        ),
                        ft.Container(
                            content=ft.Text(
                                ref=self.error_text_name,
                                value="",
                                color=ft.colors.RED_400,
                                size=12,
                                text_align=ft.TextAlign.LEFT,
                                width=360,  # Чуть меньше ширины контейнера для отступов
                                selectable=True,  # Позволяет выделять текст
                                visible=False
                            ),
                            padding=ft.padding.only(top=10, bottom=10)  # Отступы сверху и снизу
                        ),
                        ft.Text(
                            "Minimal intensity:",
                            size=14,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Slider(
                            ref=self.min_intensity,
                            min=0,
                            max=100,
                            divisions=100,
                            label="{value}%",
                            value=50,
                            on_change=self.validate_intensities,
                            width=400
                        ),
                        ft.Text(
                            "medium intensity:",
                            size=14,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Slider(
                            ref=self.avg_intensity,
                            min=0,
                            max=100,
                            divisions=100,
                            label="{value}%",
                            value=70,
                            on_change=self.validate_intensities,
                            width=400
                        ),
                        ft.Text(
                            "Maximum intensity:",
                            size=14,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Slider(
                            ref=self.max_intensity,
                            min=0,
                            max=100,
                            divisions=100,
                            label="{value}%",
                            value=90,
                            on_change=self.validate_intensities,
                            width=400
                        ),
                        ft.Container(
                            content=ft.Text(
                                ref=self.error_text_sliders,
                                value="",
                                color=ft.colors.RED_400,
                                size=12,
                                text_align=ft.TextAlign.LEFT,
                                width=360,  # Чуть меньше ширины контейнера для отступов
                                selectable=True,  # Позволяет выделять текст
                                visible=False
                            ),
                            padding=ft.padding.only(top=10, bottom=10)  # Отступы сверху и снизу
                        )
                    ],
                    tight=True,
                    spacing=10
                ),
                padding=20  # Отступы от краёв диалога
            ),
            actions=[
                ft.TextButton("Close", on_click=self.close_add_dialog),
                ft.TextButton("Add", on_click=self.add_new_sport),
            ]
        )

        self.page.dialog = self.add_sport_dialog
        self.add_sport_dialog.open = True
        self.page.update()

    def validate_intensities(self, e=None):
        """Проверяет корректность значений интенсивности"""
        if not all([self.min_intensity.current, self.avg_intensity.current, self.max_intensity.current]):
            return

        min_val = self.min_intensity.current.value
        avg_val = self.avg_intensity.current.value
        max_val = self.max_intensity.current.value

        if not (min_val <= avg_val <= max_val):
            self.error_text_sliders.current.value = (
                "the minimal intensity must be less then the medium intensity, "
                "The medium must be less than the maximum!"
            )
            self.error_text_sliders.current.visible = True
        else:
            self.error_text_sliders.current.value = ""
            self.error_text_sliders.current.visible = False

        self.page.update()

    def validate_name(self, e=None):
        # Проверяем существование спорта
        capitalized_name = self.add_sport_name_field.current.value.title()
        if capitalized_name in SPORTS:
            self.error_text_name.current.value = f"Sport '{capitalized_name}' already exists!"
            self.error_text_name.current.visible = True
        else:
            self.error_text_name.current.value = ""
            self.error_text_name.current.visible = False

        self.page.update()

    def filter_sports(self, e):
        search_term = self.search_field.current.value.lower()
        filtered = [
            sport for sport in SPORTS
            if search_term in sport.lower()
        ]

        # Если нет точного совпадения и есть текст поиска
        if (search_term and
                search_term not in [s.lower() for s in SPORTS]):
            # Добавляем опцию создания нового спорта
            filtered.append(f"Add new sport: {self.search_field.current.value}")

        self.filtered_list.current.controls = [
            ft.ListTile(
                title=ft.Text(sport),
                on_click=lambda _, s=sport: self.handle_sport_selection(s)
            ) for sport in filtered
        ]
        self.page.update()

    def handle_sport_selection(self, sport: str):
        if sport.startswith("Add new sport: "):
            # Извлекаем название нового спорта
            new_sport = sport.replace("Add new sport: ", "")
            self.close_dialog()
            self.show_add_sport_dialog(new_sport)
        else:
            self.selected_sport = sport
            self.apply_sport_change()

    def add_new_sport(self, e):
        if self.error_text_sliders.current.visible or self.error_text_name.current.visible:
            return

        sport_name = self.add_sport_name_field.current.value.title()
        self.intensities = {
            "low": self.min_intensity.current.value,
            "average": self.avg_intensity.current.value,
            "high": self.max_intensity.current.value,
        }

        if self.on_add_new_sport:
            self.on_add_new_sport(sport_name, self.intensities)

        # Добавляем в список спортов
        SPORTS[sport_name] = self.intensities
        # Обновляем текущее значение
        self.value = sport_name
        self.text_field.current.value = sport_name

        self.close_add_dialog()

    def close_dialog(self, e=None):
        self.sport_dialog.open = False
        self.page.dialog = None  # Clear the dialog from the page
        self.set_icon_button()
        self.page.update()

    def close_add_dialog(self, e=None):
        self.add_sport_dialog.open = False
        self.page.dialog = None  # Clear the dialog from the page
        self.set_icon_button()
        self.page.update()

    def apply_sport_change(self, e=None):
        if hasattr(self, 'selected_sport'):
            self.value = self.selected_sport
            self.intensities = SPORTS[self.selected_sport]
            self.text_field.current.value = self.selected_sport
            if self.on_change:
                self.on_change(self.selected_sport)
        self.close_dialog()
