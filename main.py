from flask import Flask, render_template
import config
import views


def page_not_found(e):
  return render_template('parts/error_404.html'), 404

app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)
app.register_blueprint(views.views, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)