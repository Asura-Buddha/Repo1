import csv

class User:
    def __init__(self, username = '', email = '', password = ''):
        self.username = username
        self.email = email
        self.password = password
        self.users_db = 'users.csv'
        self.friends_db = 'friends.csv'


    def get_friends(self, db, users_db):
        with open(db) as file:
            result = []
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                if (row[0] == self.username):
                    result.append(User.get_user(row[1],users_db))
                elif (row[1] == self.username):
                    result.append(User.get_user(row[0],users_db))
            return result

    def add_friend(self, friend, db):
        with open(db, 'a') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow([self.username, friend.username])


    def save_db(self, db_name):
        with open(db_name, 'a') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow([self.username, self.email, self.password])

    @staticmethod
    def get_user(username, db):
        with open(db) as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                if len(row) == 0:
                   pass
                elif (row[0] == username):
                    return User(row[0], row[1], row[2])
        return False

    @staticmethod
    def all_users(db):
        result = []
        with open(db) as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                result.append(User.get_user(row[0],'users.csv'))
        return result

    
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