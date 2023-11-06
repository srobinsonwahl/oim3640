from flask import Flask, render_template, request
from weather import get_temperature

app = Flask(__name__)


# If the website domain is www.xyz.com, http://www.xyz.com/ will trigger the function below
@app.route("/")
def index():
    return "<p>Hello, World!</p>"


# If the website domain is www.xyz.com, http://www.xyz.com/hello and http://www.xyz.com/hello/<name> will trigger the function below
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        return render_template('hello.html', username = name)
    return "<h1>Hello, guest!</h1>"


# Create another route like '/square/<num>', so the web app will display the square of the number
@app.route('/square/<num>')
def square(num=None):
    if num:
        result = float(num) ** 2
        return f'The square of {num} is {result}.'
    return 'You need to provide a number.'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/weather/', methods=['GET', 'POST'])
def get_weather():
    if request.method == 'POST':
        city_name = request.form('city')
        temp = get_temperature(city_name)

        return f'The current temperature of the city {city_name} is {temp}.'
    else:
        return render_template('weather-form.html')


if __name__ == "__main__":
    app.run(debug=True)
