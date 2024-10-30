'''
>>> params = UserParameters()
>>> bool(params)
False
>>> # Установка значений
>>> params.name = "John Doe"
>>> params.age = 25
>>> params.gender = Gender.MALE  # Можно использовать Enum
>>> params.gender = "Male"       # Или строку - автоматически преобразуется в Enum
>>> # Получение значений
>>> params.name
'John Doe'
>>> params.gender
<Gender.MALE: 'Male'>
>>> params.gender.value
'Male'
>>> bool(params)
True
>>> # Преобразование в словарь
>>> params.to_dict()
{'name': 'John Doe', 'gender': <Gender.MALE: 'Male'>, 'age': 25, 'weight': 0, 'height': 0, 'main_sport': None, 'training_times': 0, 'activity_level': <ActivityLevel.SEDENTARY: 'sedentary'>, 'goal': <Goal.CUT: 'cut'>, 'allergies': []}
>>> params.main_sport = Sport("example", {"low": 0, "average": 0, "high": 0})
>>> params.main_sport
Sport(name='example', intensities={'low': 0, 'average': 0, 'high': 0})
'''

from enum import Enum

from data.client_storage_data import ClientStorageClass
from data.sports import Sport


class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"


class Goal(str, Enum):
    CUT = "Cut"
    BULK = "Bulk"
    MAINTAIN = "Stay the same"
    NO_GOALS = "No goals yet"


class ActivityLevel(str, Enum):
    """Additional activity levels"""
    SEDENTARY = "Sedentary"
    LIGHTLY_ACTIVE = "Lightly active"
    ACTIVE = "Active"
    HIGHLY_ACTIVE = "Highly active"


class UserParameters(ClientStorageClass):
    name: str
    gender: Gender
    age: int
    weight: int
    height: int
    main_sport: Sport
    training_times: int
    activity_level: ActivityLevel
    goal: Goal
    allergies: list[str]
