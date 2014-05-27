from app import app
from forms import Registration
from flask import render_template #, flash, redirect

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = Registration()
    return render_template('index.html', form=form)