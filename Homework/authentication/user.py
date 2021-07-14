import csv

class User:
    def __init__(self, username = '', email = '', password = ''):
        self.username = username
        self.email = email
        self.password = password
        


    def get_friends(self, friend_db, users_db):
        with open(friend_db) as file:
            result = []
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                if (row[0] == self.username):
                    result.append(User.get_user(row[1],users_db))
                elif (row[1] == self.username):
                    result.append(User.get_user(row[0],users_db))
            return result

    def add_friend(self, friend, friend_db):
        with open(friend_db, 'a') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow([self.username, friend.username])


    def save_db(self, db_name):
        with open(db_name, 'a') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow([self.username, self.email, self.password])

    @staticmethod
    def get_user(username, user_db):
        with open(user_db) as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                if (row[0] == username) or row[1] == username:
                    return User(row[0], row[1], row[2])
        return False


    
    def __str__(self):
        return self.username + ' (' + self.email + ')'
    def __repr__(self):
        return self.username + ' (' + self.email + ')'



def main():
    db = 'users.csv'

    # dan = User('dan', 'dan@gmail.com', '123123')
    # adil = User('adil', 'adil@gmail.com', '123123123')
    # john = User('john', 'john@gmail.com', '321321')

    dan = User.get_user('dan',db)
    dan.add_friend(User.get_user('adil',db), 'friends.csv')
    print(dan.get_friends('friends.csv', db))    


if __name__ == '__main__':
    main()

# dan, dan@dan.com, dandandan123