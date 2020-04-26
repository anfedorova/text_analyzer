import itertools
from app import app, db
from flask import request, redirect, url_for
from forms import AnalyzeForm
from flask import render_template
from analyze_text import AnalyzeText
from scripts import load_file, create_records
from model import Texts

STYLE = {
    'sientific': 'науковий',
    'officially_business': 'офіційно-діловий',
    'artistic': 'художній',
    'conversational': 'розмовний'
}


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AnalyzeForm()

    if request.method == 'POST' and form.validate_on_submit():
        filename = load_file(form.data.data)
        choice = form.choice.data
        analyze_text = AnalyzeText(app.config['UPLOAD_TEXT'] + filename)
        result = analyze_text.generate_result()

        create_records(result, choice)

        result = dict(itertools.islice(result.items(), 30))
        return render_template('index.html', form=form, text=analyze_text.text, result=result)

    return render_template('index.html', form=form)


@app.route('/sientific', methods=['GET'])
def sientific():
    sientific_all = Texts.query.filter(Texts.type == STYLE['sientific'])

    return render_template('sientific.html', result=sientific_all)


@app.route('/officially_business', methods=['GET'])
def officially_business():
    officially_business_all = Texts.query.filter(Texts.type == STYLE['officially_business'])

    return render_template('officially_business.html', result=officially_business_all)


@app.route('/artistic', methods=['GET'])
def artistic():
    artistic_all = Texts.query.filter(Texts.type ==STYLE['artistic'])

    return render_template('artistic.html', result=artistic_all)


@app.route('/conversational', methods=['GET'])
def conversational():
    conversational_all = Texts.query.filter(Texts.type == STYLE['conversational'])

    return render_template('conversational.html', result=conversational_all)


@app.route('/delete/<id>')
def delete(id):
    if id == '*':
        Texts.query.delete()
    else:
        Texts.query.filter_by(id=id).delete()

    db.session.commit()

    return redirect(url_for(request.args.get('template')))