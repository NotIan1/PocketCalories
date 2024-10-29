from enum import Enum
from typing import get_type_hints, Type, Any

import flet as ft
from flet_core.client_storage import ClientStorage


class ClientStorageMetaclass(type):
    """Метакласс для автоматического создания property с поддержкой client_storage"""

    def __new__(mcs, name: str, bases: tuple, attrs: dict):
        # Получаем аннотации типов
        type_hints = attrs.get('__annotations__', {})

        # Создаем property для каждой аннотации
        for field_name, field_type in type_hints.items():
            # Пропускаем специальные атрибуты
            if field_name.startswith('__'):
                continue

            # Создаем property
            attrs[field_name] = mcs.create_property(field_name, field_type)

        return super().__new__(mcs, name, bases, attrs)

    @staticmethod
    def get_default(t: Type) -> Any:
        """Определяет значение по умолчанию на основе типа"""
        if hasattr(t, '__origin__') and t.__origin__ is list:
            return []
        if issubclass(t, Enum):
            return list(t)[0]  # Первое значение enum
        elif t == str:
            return ''
        elif t == int:
            return 0
        elif t == float:
            return 0.0
        elif t == bool:
            return False
        return None

    @classmethod
    def create_property(mcs, field_name: str, field_type: Type) -> property:
        """Создает property для заданного поля"""
        private_name = f'_{field_name}'  # Эта переменная теперь уникальна для каждого property

        def getter(self):
            if not hasattr(self, private_name):
                value = self._client_storage.get(field_name)
                if value is None:
                    value = mcs.get_default(field_type)
                # Преобразуем значение в правильный тип
                if issubclass(field_type, Enum):
                    value = field_type(value) if value else mcs.get_default(field_type)
                setattr(self, private_name, value)
            return getattr(self, private_name)

        def setter(self, value):
            # Валидация типа
            if value is not None:
                if issubclass(field_type, Enum):
                    if not isinstance(value, field_type):
                        value = field_type(value)
                elif not isinstance(value, list) and not isinstance(value, field_type):
                    try:
                        value = field_type(value)
                    except (ValueError, TypeError) as e:
                        raise TypeError(
                            f"Expected {field_type.__name__}, got {type(value).__name__}: {e}"
                        )

            setattr(self, private_name, value)
            self._client_storage.set(
                field_name,
                value if not isinstance(value, Enum) else value.value
            )

        return property(getter, setter)

class InMemoryClientStorage(ClientStorage):
    def __init__(self, page=None):
        super().__init__(page)
        self._values = {}

    def get(self, key: str) -> Any:
        return self._values.get(key)

    def set(self, key: str, value: Any) -> None:
        self._values[key] = value


class ClientStorageClass(metaclass=ClientStorageMetaclass):
    """Базовый класс для классов с поддержкой client_storage"""

    def __init__(self, client_storage: ClientStorage = InMemoryClientStorage()):
        self._client_storage = client_storage

    @classmethod
    def create(cls, page: ft.Page) -> 'ClientStorageClass':
        """Фабричный метод для создания экземпляра с client_storage из page"""
        return cls(page.client_storage)

    def to_dict(self) -> dict:
        """Преобразует все поля в словарь"""
        return {
            name: getattr(self, name)
            for name in get_type_hints(self.__class__)
            if not name.startswith('__')
        }
