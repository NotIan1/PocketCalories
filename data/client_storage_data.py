import dataclasses
import typing
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

    @staticmethod
    def is_default_value(value: Any, type_: Type) -> bool:
        """Проверяет, является ли значение значением по умолчанию для данного типа"""
        default = ClientStorageMetaclass.get_default(type_)

        # Для списков проверяем на пустоту
        if typing.get_origin(type_) is list:
            return len(value) == 0

        # Для строк проверяем на пустоту
        if type_ is str:
            return not bool(value.strip())

        # Для чисел проверяем на 0
        if type_ in (int, float):
            return value == 0

        # Для Enum проверяем, является ли значение первым элементом enum
        if issubclass(type_, Enum):
            return value == list(type_)[0]

        # Для остальных типов просто сравниваем с default
        return value == default

    @staticmethod
    def validate_value(value: Any, expected_type: Type) -> Any:
        """Проверяет и преобразует значение в правильный тип"""
        # Получаем базовый тип и аргументы типа
        origin_type = typing.get_origin(expected_type)
        type_args = typing.get_args(expected_type)

        # Для списков
        if origin_type is list:
            if not isinstance(value, list):
                value = list(value) if value is not None else []
            # Если есть тип элементов списка, проверяем каждый элемент
            if type_args:
                element_type = type_args[0]
                value = [
                    element_type(item) if not isinstance(item, element_type) else item
                    for item in value
                ]
            return value

        # Для Enum
        if expected_type is not None and issubclass(expected_type, Enum):
            return expected_type(value) if not isinstance(value, expected_type) else value

        # Для простых типов
        if expected_type is not None and not isinstance(value, expected_type):
            try:
                return expected_type(value)
            except (ValueError, TypeError) as e:
                raise TypeError(
                    f"Expected {expected_type.__name__}, got {type(value).__name__}: {e}"
                )

        return value

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
                if isinstance(field_type, Enum):
                    value = field_type(value) if value else mcs.get_default(field_type)
                if dataclasses.is_dataclass(field_type):
                    value = field_type(**value) if value else mcs.get_default(field_type)
                # if issubclass(field_type, )
                setattr(self, private_name, value)
            return getattr(self, private_name)

        def setter(self, value):
            # Валидация и преобразование типа
            validated_value = mcs.validate_value(value, field_type)
            setattr(self, private_name, validated_value)

            # Для Enum сохраняем значение, для остальных типов - сам объект
            storage_value = validated_value.value if isinstance(validated_value, Enum) else validated_value
            self._client_storage.set(field_name, storage_value)

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

    def __bool__(self) -> bool:
        """
        Возвращает True, если хотя бы одно поле отличается от значения по умолчанию,
        False - если все поля имеют значения по умолчанию
        """
        for field_name, field_type in get_type_hints(self.__class__).items():
            if field_name.startswith('_'):
                continue
            value = getattr(self, field_name)
            if not self.__class__.__class__.is_default_value(value, field_type):
                return True
        return False