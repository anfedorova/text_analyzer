from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms import SelectField


class AnalyzeForm(FlaskForm):
    data = FileField('Файл', validators=[FileRequired()])
    choice = SelectField('Стиль', choices=[
        ('науковий', 'Науковий'),
        ('офіційно-діловий', 'Офіційно-діловий'),
        ('художній', 'Художній'),
        ('розмовний', 'Розмовний')
    ])
