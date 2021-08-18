from flask import Flask, request, render_template
from user import cmdApp

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.jinja')


@app.route('/encrypt')
def encrypt():
    new_img = 0
    if (request.method == 'POST'):
        # image =  flask.request.files('imagefile')
        msg = request.form["msg"]
        img = request.form["img"]
        new_img = cmdApp.encrypt(img, msg)
        # call functions from cmdApp

    return render_template('encrypt.jinja', n_img = new_img)  # Encryption page'


@app.route('/decrypt')
def decrypt():
    msg = 0
    if (request.method == 'POST'):
        s_img = request.form["s_img"]
        msg = cmdApp.decrypt(s_img, "idk what to put here")

        # call functions from cmdApp

    return render_template('decrpyt.jinja', msg = msg)  # Decryption page'


if __name__ == '__main__':
    app.run()
