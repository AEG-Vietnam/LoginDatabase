import time
import os


def get_user_database(filename):
    # return [['apple', 'sweet'], ['watermelon', '1991'], ['William', 'app_127']]
    database = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            line = line.replace('\'', '')
            if line != '':
                username, password = line.split(', ')
                database.append([username, password])
        file.close()
    return database


def add_new_user(database, username, password):
    database.append([username, password])
    with open('user_database.csv', 'a') as file:
        file.write(f"\n'{username}', '{password}'")
        file.close()
    return database


def matches(user, username, password):
    return [username, password] == user


def has_account():
    register_input = input('Are you an existing User? (y/n)')
    if 'y' == register_input.lower() or 'yes' == register_input.lower():
        return True
    elif 'n' == register_input.lower() or 'no' == register_input.lower():
        return False
    else:
        has_account()


def check_login_info(database):
    username_input = input("Please enter your Username:")
    user_found = False
    for user in database:
        if username_input == user[0]:
            user_found = True
            password_input = input("Please enter your Password:")
            if matches(user, username_input, password_input):
                return
            else:
                check_login_info(database)
    if not user_found:
        check_login_info(database)


def make_new_account(database):
    username_input = input("Please enter a new Username:")
    for user in database:
        if username_input == user[0]:
            print("That username is taken!")
            print("Please try a different username.")
            users_database = make_new_account(database)
            return users_database
    password_input = input("Please enter your password:")
    users_database = add_new_user(database, username_input, password_input)
    return users_database


def print_welcome_message(length):
    print(f"Welcome! There are currently {length} users!")


def login(database):

    print('Welcome!')

    if has_account():
        check_login_info(database)
    else:
        database = make_new_account(database)

    print_welcome_message(len(database))

    time.sleep(2)


def logout():
    wait_time = 3  # how long to wait between log in/out
    print(f"Logging you out in {wait_time} secs")
    for i in range(0, wait_time):
        time.sleep(1)
        os.system('cls')
        print(f"Logging you out in {wait_time - i -1} secs")
    os.system('cls')


if __name__ == '__main__':
    user_database = get_user_database('user_database.csv')
    while True:
        login(user_database)
        logout()
