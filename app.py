from flask import Flask, render_template, request
import logic.gpt_3 as gpt3
import config


def page_not_found(e):
  return render_template('parts/error_404.html'), 404

app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

@app.context_processor
def process():
    currentYear = config.CURRENT_YEAR
    
    return dict(currentYear=currentYear)

@app.route('/')
def index():
    return render_template('index.html', **locals())

@app.route('/openai', methods=["GET", "POST"])
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



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)