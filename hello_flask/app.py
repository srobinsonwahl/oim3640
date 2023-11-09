from flask import Flask, redirect,render_template, request
from weather import get_temperature

app = Flask(__name__)


# If the website domain is www.xyz.com, http://www.xyz.com/ will trigger the function below
# @app.route("/")
# def index():
#     return "<p>Hello, World!</p>"


# If the website domain is www.xyz.com, http://www.xyz.com/hello and http://www.xyz.com/hello/<name> will trigger the function below
@app.route('/')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        return render_template('hello.html', username = name)
    return render_template('hello.html')


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

# @app.route('/weather/', methods=['GET', 'POST'])
# def get_weather():
#     if request.method == 'POST':
#         city_name = request.form['city']
#         temp = get_temperature(city_name)

#         return f'The current temperature of the city {city_name} is {temp}.'
#     else:
#         return render_template('weather-form.html')

@app.get('/weather/')
def weather_get():
    return render_template('weather-form.html')

@app.post('/weather/')
def weather_post():
    city_name = request.form['city']
    temp = get_temperature(city_name)
    return f'The current temperature of the city {city_name} is {temp}.'

STUDENTS = {}
COURSES = ['Python', 'Web', 'Cybersecurity', 'Mobile App']

@app.route('/students/')
def show_students():
    return render_template('students.html', students = STUDENTS, courses = COURSES)

@app.get('/register/')
def register_get():
    return render_template('/register-form.html')

@app.post('/register/')
def register_post():
    name = request.form['name']
    course = request.form['course']
    if course not in COURSES:
        return 'Hi hacker, you cannot register this course!'
    STUDENTS[name] = course
    return redirect('/students/')

if __name__ == "__main__":
    app.run(debug=True)
