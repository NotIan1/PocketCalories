'''
>>> age = 40
>>> weight = 90 # kg
>>> height = 176 # cm
>>> sport = Sport("No Sport", SPORTS["No Sport"])
>>> intensity = "high"
>>> weight_goal = "Stay the same"  # Can be "cut", "bulk", or "stay the same"
>>> gender = "Male"
>>> sessions_per_week = 0
>>> additional_activity = "lightly active"
>>> calories_needed = calculate_calories(age, weight, height, sport, intensity, weight_goal, gender, sessions_per_week,additional_activity)
>>> print(f"Calories needed per day: {calories_needed}")
Calories needed per day: 1620
'''

from data.sports import SPORTS, Sport, SportIntensity
from data.user_params import Gender, Goal, ActivityLevel


def calculate_activity_factor(sessions_per_week: int, sport: Sport, sport_intensity: SportIntensity, additional_activity: ActivityLevel):
    # Step 1: Base Factor from Sessions per Week
    if sessions_per_week <= 1:
        base_factor = 1.2  # Sedentary
    elif sessions_per_week in [2, 3]:
        base_factor = 1.375  # Lightly Active
    elif sessions_per_week in [4, 5]:
        base_factor = 1.55  # Moderately Active
    elif sessions_per_week in [6, 7]:
        base_factor = 1.725  # Very Active
    else:
        base_factor = 1.9  # Super Active

    # Step 2: Adjust based on Sport Intensity (in %)
    intensity_factor = sport.intensities[sport_intensity] / 100  # Convert % to a decimal
    adjusted_factor = base_factor * (1 + (intensity_factor - 0.5) / 2)

    # Step 3: Adjust based on Additional Activity
    if additional_activity == ActivityLevel.SEDENTARY:
        additional_activity_adjustment = 0  # No change
    elif additional_activity == ActivityLevel.LIGHTLY_ACTIVE:
        additional_activity_adjustment = 0.05
    elif additional_activity == ActivityLevel.ACTIVE:
        additional_activity_adjustment = 0.1
    elif additional_activity == ActivityLevel.HIGHLY_ACTIVE:
        additional_activity_adjustment = 0.2
    else:
        additional_activity_adjustment = 0  # Default to no change if input is unexpected

    # Step 4: Calculate Final Activity Factor
    final_activity_factor = adjusted_factor + additional_activity_adjustment
    return final_activity_factor

def calculate_bmr(age: int, weight: int, height: int, gender: Gender):
    if gender == Gender.MALE:
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == Gender.FEMALE:
        return 10 * weight + 6.25 * height - 5 * age - 161


def adjust_for_goal(calories: int, weight_goal: Goal):
    if weight_goal == Goal.BULK:
        return calories + 300  # Add extra calories for bulking
    elif weight_goal == Goal.CUT:
        return calories - 500  # Subtract calories for cutting
    else:
        return calories  # No adjustment for maintenance


def calculate_calories(age: int, weight: int, height: int,
                       main_sport: Sport, intensity: SportIntensity, goal: Goal,
                       gender: Gender, training_times: int, activity_level: ActivityLevel,
                       **kwargs):
    # Step 1: Calculate BMR
    bmr = calculate_bmr(age, weight, height, gender)

    # Step 2: Calculate activity factor
    activity_factor = calculate_activity_factor(training_times, main_sport, intensity, activity_level)

    # Step 3: Adjust BMR for activity
    tdee = bmr * activity_factor

    # Step 4: Adjust for weight goal (cutting, bulking, or maintaining)
    final_calories = adjust_for_goal(tdee, goal)

    return int(round(final_calories / 10) * 10)



if __name__ == '__main__':
    age = 40
    weight = 90 # kg
    height = 176 # cm
    sport = Sport("No Sport", SPORTS["No Sport"])
    intensity = "high"
    weight_goal = "Stay the same"  # Can be "cut", "bulk", or "stay the same"
    gender = "Male"
    sessions_per_week = 0
    additional_activity = "lightly active"

    calories_needed = calculate_calories(age, weight, height, sport, intensity, weight_goal, gender, sessions_per_week,additional_activity)
    print(f"Calories needed per day: {calories_needed}")

