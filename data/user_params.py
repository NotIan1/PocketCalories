'''
>>> params = UserParameters()
>>> # Установка значений
>>> params.name = "John Doe"
>>> params.age = 25
>>> params.gender = Gender.MALE  # Можно использовать Enum
>>> params.gender = "male"       # Или строку - автоматически преобразуется в Enum
>>> # Получение значений
>>> params.name
'John Doe'
>>> params.gender
<Gender.MALE: 'male'>
>>> params.gender.value
'male'
>>>
>>> # Преобразование в словарь
>>> params.to_dict()
{'name': 'John Doe', 'gender': <Gender.MALE: 'male'>, 'age': 25, 'weight': 0, 'height': 0, 'main_sport': '', 'training_times': 0, 'activity_level': <ActivityLevel.SEDENTARY: 'sedentary'>, 'goal': <Goal.CUT: 'cut'>, 'allergies': []}
'''

from enum import Enum

from data.client_storage_data import ClientStorageClass


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
    main_sport: str
    training_times: int
    activity_level: ActivityLevel
    goal: Goal
    allergies: list[str]
