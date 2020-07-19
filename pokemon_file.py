def create_trainer():
    user_info = {
        'User': [
        ],
        'Pokemon': [
        ],
    }

    add_trainer = input("Do you want to add a trainer? (yes/no) ")
    if add_trainer == 'no':
        quit()
    else:
        user_info['User'].append(user_name())

    while True:
        add_pokemon = input("Do you want to add a Pokemon? (yes/no) ")
        if add_pokemon == 'no':
            add_trainer = input("Do you want to add a trainer? (yes/no) ")
            if add_trainer == 'no':
               break
            else:
                user_info['User'].append(user_name())
        else:
            user_info['Pokemon'].append(create_pokemon())

    print(user_info)


def create_pokemon():
    return {'Pokemon name': input("What is your Pokemon? ").title(),
            'Pokemon level': input("What level is your Pokemon? "),
            'Pokemon type': input("What is your Pokemon's type? ").title()}


def user_name():
    return {'First_Name': input("What is your first name? ").title(),
            'Last_Name': input("What is your last name? ").title()}

