# python -m venv env
from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required

#from webapp.news import get_python_news
from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.news.views import blueprint as news_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/start')
    def start():
        title = "Start"
        #login_form = LoginForm()
        return render_template('3D/d10_d11_login.html')
        #return render_template('3D/d3_make_order.html')

    return app

        #weather = False
        #if weather:
        #    weather_text = f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
        #else:
        #    weather_text = "Прогноз сейчас недоступен"
        #return f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"

#if __name__=="__main__":
#    app.run(debug=True)