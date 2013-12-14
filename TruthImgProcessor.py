import os
from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from werkzeug import secure_filename
import settings

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = settings.MEDIA_ROOT
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS_AVATAR = set(['png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'jpg', 'jpeg', 'png', 'gif'])


def allowed_file(filename, avatar=False):
    a = ALLOWED_EXTENSIONS
    if avatar:
        a = ALLOWED_EXTENSIONS_AVATAR
    return '.' in filename and filename.rsplit('.', 1)[1] in a


@app.route('/upload_file', methods=['POST'])
def upload_file():
    ufile = request.files['file']
    if ufile and allowed_file(ufile.filename):
        filename = secure_filename(ufile.filename)
        ufile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))

@app.route('/upload_avatar', methods=['POST'])
def upload_avatar():
    ufile = request.files['file']
    if ufile and allowed_file(ufile.filename, avatar=True):
        filename = secure_filename(ufile.filename)
        ufile.save(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + settings.AVATAR_UPLOAD_DIR, filename))
        return redirect(url_for('uploaded_file', filename=filename))

if __name__ == '__main__':
    app.run()
