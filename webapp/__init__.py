# python -m venv env
from flask import Flask
from flask import render_template
from webapp.weather import weather_by_city
from webapp.news import get_python_news

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    @app.route("/") #main site page
    def index():
        title = 'Новости Python'
        weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        news_list = get_python_news()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)

    return app

        #weather = False
        #if weather:
        #    weather_text = f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
        #else:
        #    weather_text = "Прогноз сейчас недоступен"
        #return f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"

#if __name__=="__main__":
#    app.run(debug=True)