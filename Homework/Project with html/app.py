from flask import Flask, request, render_template, Response
from utils import encrypt as enc
from utils import decrypt as dec
from PIL import Image

import io

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        if (request.form['s_msg']):
            img = Image.open(request.files['s_img'].stream)
            msg = dec(img, "123")
            return render_template('index.html', s_msg=msg)  # Decryption page'
        else:
            # image =  flask.request.files('imagefile')
            msg = request.form["msg"]
            # img = request.form["img"]
            img = Image.open(request.files['img'].stream)
            new_img = enc(msg, img, '123')
            new_img.save('static/' + request.files['img'].filename)
            name = request.files['img'].filename
            return render_template('index.html', e_img=name)  # Encryption page'

    return render_template('index.html')


'''@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    name = ''
    if (request.method == 'POST'):
        # image =  flask.request.files('imagefile')
        msg = request.form["msg"]
        # img = request.form["img"]
        img = Image.open(request.files['img'].stream)
        new_img = enc(msg, img, '123')
        new_img.save('static/' + request.files['img'].filename)
        name = request.files['img'].filename
    return render_template('encrypt.jinja', name=name)  # Encryption page'


@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    msg = ''
    if (request.method == 'POST'):
        img = Image.open(request.files['s_img'].stream)
        msg = dec(img, "123")

    return render_template('decrypt.jinja', s_msg=msg)  # Decryption page''''

if __name__ == '__main__':
    app.run(debug=True)
