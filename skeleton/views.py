from crypt import methods
from symbol import decorators
from flask import Blueprint, render_template, request, redirect
from flask_mail import Mail, Message
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .config import config
from . import db, g_app
from .modules.gpt3 import gpt3


views = Blueprint('views', __name__)
mail = Mail(g_app)
limiter = Limiter(g_app, key_func=get_remote_address)


@views.context_processor
def process():
    currentYear = config['development'].CURRENT_YEAR

    return dict(currentYear=currentYear)


@views.route('/')
def index():
    return render_template('index.html', **locals())


@views.route('/about')
def about():
    return render_template('about.html', **locals())


@views.route('/projects')
def projects():
    return render_template('projects.html', **locals())


@views.route('/openai', methods=["GET", "POST"])
def openai():
    if request.method == 'POST':
        if 'ai_form' in request.form:
            input_text = request.form['TextResult']
            response = gpt3.text_model(input_text)
            response = response[2:]
            Result = response.replace('?', '')

    return render_template('openai.html', **locals())


@views.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        if 'contact_form' in request.form:
            name = request.form['name']
            email = request.form['email']
            subject = request.form['subject']
            message = request.form['message']

            msg = Message(subject, sender=email, recipients=['website@mcjkula.com'])
            msg.body = msg.body = 'Nachricht von ' + name + ',\n \n' + \
                message + '\n \n' + 'Melden an diese E-Mail: ' + email
            msg.html = render_template(
                '/mails/contact_mail.html',name=name, message=message, email=email)
            mail.send(msg)

            return redirect('/contact/success')

    return render_template('contact/form_page.html', **locals())


@views.route('/contact/success', methods=["POST"])
@limiter.limit("5/day")
def contact_success():
    return render_template('contact/success.html', **locals())
