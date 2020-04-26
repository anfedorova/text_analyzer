import os
from app import app, db
from werkzeug.utils import secure_filename
from model import Texts


def create_folder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except PermissionError:
        print("Path not found")
        exit()


def load_file(file):
    create_folder(app.config['UPLOAD_TEXT'])

    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_TEXT'], filename))

    return filename


def create_records(result, style):
    for key in result:
        record = Texts.query.filter(Texts.chars == key, Texts.type == style).first()
        if record:
            record.frequency += result[key]
        else:
            model = Texts(chars=key, frequency=result[key], type=style)
            db.session.add(model)
        db.session.commit()
