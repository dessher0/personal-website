from flask import Blueprint, render_template, request

js_views = Blueprint('js_views', __name__)


@js_views.route('/languages')
def languages():
    language_of_frameworks = {
        'python': ['Flask', 'Django', 'FastAPI'],
        'javascript': ['Express', 'React', 'Vue', 'Angular'],
        'php': ['Laravel', 'Symfony', 'CodeIgniter'],
    }

    language = request.args.get('language')
    list_of_frameworks = language_of_frameworks[language]

    return render_template('/javascript/languages.html', list_of_frameworks=list_of_frameworks)
