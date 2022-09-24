from flask import Blueprint, render_template, request
from .config import config
from .logic import gpt_3 as gpt3

views = Blueprint('views', __name__)

@views.context_processor
def process():
    currentYear = config['development'].CURRENT_YEAR
    
    return dict(currentYear=currentYear)

@views.route('/')
def index():
    return render_template('index.html', **locals())

@views.route('/openai', methods=["GET", "POST"])
def openai():
    if request.method == 'POST':
        if 'form_1' in request.form:
            input_text = request.form['TextResult']
            response = gpt3.text_model(input_text)
            response = response[2:]
            Result = response.replace('?', '')
    return render_template('openai.html', **locals())

# @app.route('/projects')
# def projects():
#     return render_template('projects.html', **locals())

# @app.route('/contact')
# def contact():
#     return render_template('contact.html', **locals())