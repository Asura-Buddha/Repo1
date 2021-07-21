from flask import Flask, render_template, redirect, session, request, url_for
from user import User

app = Flask(__name__)
app.secret_key = 'QWERTYUJHGFDSWERTYUJKasdasd'


# home page
@app.route('/')
def index():
    if (session.get('user')):
        return redirect(url_for('users'))

    return render_template('index.jinja')


# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        username = request.form["usr"]
        password = request.form["pss"]
        if User.get_user(username, 'users.csv'):
            tmp = User.get_user(username, 'users.csv')
            if password == tmp[2]:
                session['user'] = username
                redirect(url_for("index"))
                '''user logged in'''
        else:
            pass
            '''notify user that name or pass is incorrect, send bak to login page'''
    return render_template('login.jinja')


# register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        nm = request.form['nm']
        mail = request.form['mail']
        ps1 = request.form['ps1']
        ps2 = request.form['ps2']
        if not User.get_user(nm,'users.csv'):
            if ps1 == ps2:
                tmp = User(nm,mail,ps1)
                tmp.save_db('users.csv')
                return redirect(url_for('login'))
            else:
                pass
                # not sure how to return register with just 1 thing changed
        else:
            pass
            # same problem but with "username has been taken"
    return render_template('register.jinja')


# all users
@app.route('/users')
def users():
    users = User.all_users('users.csv')
    return render_template('users.jinja', users=users)


# user
@app.route('/users/<username>')
def user(username):
    my_user = User.get_user(username, 'users.csv')

    return render_template('user.jinja', my_user=my_user)


if __name__ == '__main__':
    app.run()
