from user import User

def main():
    print("Would you like to register? Y or N: ")
    if input() == 'Y':
        name = input("Please enter a username: ")
        email = input("Please input your email: ")
        ps1 = input("Please input your password: ")
        ps2 = input("Please repeat your password (It is case-sensitive): ")
        while(ps1 != ps2):
            print("Repeated password does not match")
            ps2 = input("Please repeat your password (It is case-sensitive): ")
        new_user = User(name,email,ps1)
        new_user.save_db('users.csv')
        print(new_user.username) #used for checking if user was made
        print(new_user.email)
        print(new_user.password)
main()