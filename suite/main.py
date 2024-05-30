from flask import Flask, render_template, request, url_for, redirect
from form import SendForm
from werkzeug.utils import secure_filename
import os



app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '123456789'

UPLOAD_FOLDER = os.path.join(app.instance_path, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=["GET", "POST"])
def start():
    form = SendForm()
    print(form.errors)
    if form.validate_on_submit():
        name = form.name.data
        filename = secure_filename(form.file.data)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(file_path)
        return redirect(url_for('upload'))
    # if request.method == 'POST':
    #     print(1)
    #     name = request.form.get('name')
    #     file = request.form.get('file')
    #     print(name, file)
    #     with open(file, 'r') as f:
    #         print(f.read())
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)