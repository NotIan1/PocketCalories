from dataclasses import dataclass
from enum import Enum


class SportIntensity(str, Enum):
    LOW, AVERAGE, HIGH = "low", "average", "high"

@dataclass
class Sport:
    name: str
    intensities: dict[SportIntensity, float]

    def __str__(self):
        return self.name


SPORTS = {
    "Swimming": {"low": 70, "high": 90, "average": 80},
    "Running": {"low": 70, "high": 85, "average": 78},
    "Cycling": {"low": 65, "high": 85, "average": 75},
    "Football": {"low": 75, "high": 90, "average": 83},
    "Basketball": {"low": 75, "high": 90, "average": 83},
    "Tennis": {"low": 70, "high": 85, "average": 78},
    "Volleyball": {"low": 60, "high": 75, "average": 68},
    "Badminton": {"low": 65, "high": 80, "average": 73},
    "Table Tennis": {"low": 50, "high": 70, "average": 60},
    "Golf": {"low": 35, "high": 50, "average": 43},
    "Boxing": {"low": 85, "high": 95, "average": 90},
    "Martial Arts": {"low": 80, "high": 90, "average": 85},
    "Yoga": {"low": 40, "high": 60, "average": 50},
    "Pilates": {"low": 50, "high": 65, "average": 58},
    "Weightlifting": {"low": 70, "high": 90, "average": 80},
    "CrossFit": {"low": 85, "high": 95, "average": 90},
    "Rowing": {"low": 70, "high": 85, "average": 78},
    "Skiing": {"low": 70, "high": 85, "average": 78},
    "Snowboarding": {"low": 60, "high": 75, "average": 68},
    "Surfing": {"low": 60, "high": 80, "average": 70},
    "Rock Climbing": {"low": 70, "high": 85, "average": 78},
    "Hiking": {"low": 50, "high": 70, "average": 60},
    "Dance": {"low": 60, "high": 80, "average": 70},
    "Gymnastics": {"low": 75, "high": 90, "average": 83},
    "Squash": {"low": 80, "high": 90, "average": 85},
    "No Sport": {"low": 0, "high": 0, "average": 0},
}
