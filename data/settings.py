from enum import Enum
from data.client_storage_data import ClientStorageClass

class UnitSystem(str, Enum):
    METRIC = "Metric"
    IMPERIAL = "Imperial"

class Settings(ClientStorageClass):
    dark_mode: bool = False
    unit_system: UnitSystem = UnitSystem.METRIC

    @staticmethod
    def convert_weight(value: float, from_system: UnitSystem, to_system: UnitSystem) -> float:
        """Convert weight between metric and imperial systems"""
        if from_system == to_system:
            return value
        if from_system == UnitSystem.METRIC and to_system == UnitSystem.IMPERIAL:
            return value * 2.20462  # kg to lbs
        return value / 2.20462  # lbs to kg

    @staticmethod
    def convert_height(value: float, from_system: UnitSystem, to_system: UnitSystem) -> float:
        """Convert height between metric and imperial systems"""
        if from_system == to_system:
            return value
        if from_system == UnitSystem.METRIC and to_system == UnitSystem.IMPERIAL:
            return value * 0.393701  # cm to inches
        return value / 0.393701  # inches to cm

    def apply_theme(self, page):
        """Apply dark or light theme to the page"""
        if self.dark_mode:
            page.theme_mode = "dark"
            page.bgcolor = "#1a1a1a"
            page.update()
        else:
            page.theme_mode = "light"
            page.bgcolor = "#F0F4FF"
            page.update()