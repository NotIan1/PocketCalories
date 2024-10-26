from sports import SPORTS


def calculate_activity_factor(sessions_per_week, sport, sport_intensity, additional_activity):
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
    intensity_factor = SPORTS[sport][sport_intensity] / 100  # Convert % to a decimal
    adjusted_factor = base_factor * (1 + (intensity_factor - 0.5) / 2)

    # Step 3: Adjust based on Additional Activity
    if additional_activity == "sedentary":
        additional_activity_adjustment = 0  # No change
    elif additional_activity == "lightly active":
        additional_activity_adjustment = 0.05
    elif additional_activity == "active":
        additional_activity_adjustment = 0.1
    elif additional_activity == "highly active":
        additional_activity_adjustment = 0.2
    else:
        additional_activity_adjustment = 0  # Default to no change if input is unexpected

    # Step 4: Calculate Final Activity Factor
    final_activity_factor = adjusted_factor + additional_activity_adjustment
    return final_activity_factor

def calculate_bmr(age, weight, height, gender):
    if gender == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == "female":
        return 10 * weight + 6.25 * height - 5 * age - 161


def adjust_for_goal(calories, weight_goal):
    if weight_goal == "bulk":
        return calories + 300  # Add extra calories for bulking
    elif weight_goal == "cut":
        return calories - 500  # Subtract calories for cutting
    else:
        return calories  # No adjustment for maintenance


def calculate_calories(age, weight, height, sport, intensity, weight_goal, gender, sessions_per_week,
                       additional_activity):
    # Step 1: Calculate BMR
    bmr = calculate_bmr(age, weight, height, gender)

    # Step 2: Calculate activity factor
    activity_factor = calculate_activity_factor(sessions_per_week, sport, intensity, additional_activity)

    # Step 3: Adjust BMR for activity
    tdee = bmr * activity_factor

    # Step 4: Adjust for weight goal (cutting, bulking, or maintaining)
    final_calories = adjust_for_goal(tdee, weight_goal)

    return round(final_calories)



if __name__ == '__main__':
    age = 40
    weight = 90 # kg
    height = 176 # cm
    sport = "No Sport"
    intensity = "high"
    weight_goal = "stay the same"  # Can be "cut", "bulk", or "stay the same"
    gender = "male"
    sessions_per_week = 0
    additional_activity = "lightly active"

    calories_needed = calculate_calories(age, weight, height, sport, intensity, weight_goal, gender, sessions_per_week,additional_activity)
    print(f"Calories needed per day: {calories_needed}")

