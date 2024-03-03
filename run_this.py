import menu

def get_user_choice(prompt, choices):
    """
    Asks the user to make a choice based on the provided prompt and choices.

    Parameters:
    - prompt: The question to display to the user.
    - choices: A dictionary mapping the user's input to the desired output.

    Returns:
    The choice corresponding to the user's input.
    """
    while True:
        print(prompt)
        for key, value in choices.items():
            print(f"{key}. {value['display']}")
        choice = input()
        
        if choice in choices:
            return choices[choice]['value']
        else:
            print("Please enter a valid number.")

meal_choices = {
    "1": {"display": "Breakfast", "value": "Breakfast"},
    "2": {"display": "Lunch", "value": "Lunch"},
    "3": {"display": "Dinner", "value": "Dinner"},
}

hall_choices = {
    "1": {"display": "Ban Righ", "value": "banRighHall"},
    "2": {"display": "Leonard Hall", "value": "leonardHall"},
    "3": {"display": "Jean-Royce Hall", "value": "jeanRoyceHall"},
}

meal_choice = get_user_choice("Which meal do you want? (Enter number)", meal_choices)
hall_choice = get_user_choice("Which dining hall do you want to check? (Enter number)", hall_choices)
driver = menu.setup_driver()

print(menu.get_menu(driver, meal_choice, hall_choice))
