from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        celsius = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return f"""
        <h1>Temperature Conversion</h1>
        <p>{celsius}°C is equal to {fahrenheit}°F</p>
        """
    except ValueError:
        return "<h1>Invalid Input</h1><p>Please enter a valid numeric value for Celsius.</p>"


if __name__ == '__main__':
    app.run()
