from user import User

def main():
    print("-----Login-----")
    name_or_email = input("Username or Email: ")
    pswrd = input("Password: ")
    if User.get_user(name_or_email,'users.csv'):
        tmp_user = User.get_user(name_or_email,'users.csv')
        if tmp_user.password == pswrd:
            print("Thank you")
            logged_in(tmp_user)
        else:
            answer = input("The username/email or password does not match. Would you like to try again? Y or N: ")
            if answer == 'Y':
                main()
            else:
                print("Goodbye")
def logged_in(user1):
    print("Here is a list of actions that you can do: ")
    print("1. Get a list of your friends")
    print("2. Add a friend")
    print("More to come in the future")
    sw = True
    while sw:
        n = int(input("Please enter the number of the action you wish to do: "))
        if n == 1:
            print("Here is a list of your friends: ")
            print(user1.get_friends('friends.csv','users.csv'))
            inp = input("Would you like to do anything else? Y or N: ")
            if inp == 'N':
                sw = False
                print("Goodbye")
        elif n == 2:
            inp = input("Who would you like to add? (Enter their username): ")
            user1.add_friend(User.get_user(inp,'users.csv'),'friends.csv')
            inp = input("Would you like to do anything else? Y or N: ")
            if inp == 'N':
                sw = False
                print("Goodbye")
main()


