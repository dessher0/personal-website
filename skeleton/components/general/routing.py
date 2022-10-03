from flask import Blueprint, render_template, request
from flask_mail import Mail, Message
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_httpauth import HTTPBasicAuth
from ...config import config
from ... import g_app
from ...models.users import users
from ...apps.gpt3 import gpt3
from werkzeug.security import check_password_hash


views = Blueprint("views", __name__)
mail = Mail(g_app)
limiter = Limiter(g_app, key_func=get_remote_address)
auth = HTTPBasicAuth()


@auth.error_handler
def auth_error():
    return render_template("errors/403.html")

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


@views.context_processor
def process():
    currentYear = config["development"].CURRENT_YEAR

    return dict(currentYear=currentYear)

@views.route("/")
def index():
    return render_template("general/index.html", **locals())


@views.route("/about")
def about():
    return render_template("general/about.html", **locals())


@views.route("/projects")
@auth.login_required
def projects():
    return render_template("general/projects.html", **locals())


@views.route("/games")
@auth.login_required
def games():
    return render_template("general/games.html", **locals())


@views.route("/openai", methods=["GET", "POST"])
def openai():
    if request.method == "POST":
        if "ai_form" in request.form:
            input_text = request.form["TextResult"]
            response = gpt3.text_model(input_text)
            response = response[2:]
            Result = response.replace("?", "")

    return render_template("general/openai.html", **locals())


@views.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("general/contact/form_page.html", **locals())


@views.route("/contact/success", methods=["POST"])
@limiter.limit(config["development"].LIMITER_DEFAULT)
def contact_success():
    if "contact_form" in request.form:
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        msg = Message(
            subject,
            sender=config["development"].MAIL_DEFAULT_SENDER,
            recipients=[config["development"].MAIL_DEFAULT_RECIPIENT]
        )
        msg.body = (
            "Nachricht von "
            + name
            + ",\n \n"
            + message
            + "\n \n"
            + "Melden an diese E-Mail: "
            + email
        )
        msg.html = render_template(
            "/mails/contact_mail.html", name=name, message=message, email=email
        )

        mail.send(msg)

    return render_template("general/contact/success.html", **locals())
