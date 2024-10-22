def calculate_activity_factor(sessions_per_week, sport_intensity, additional_activity):
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
    intensity_factor = sport_intensity / 100  # Convert % to a decimal
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


if __name__ == '__main__':
    my_activity=calculate_activity_factor(6,75,"lightly active")
    print(my_activity)

