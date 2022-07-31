from Adafruit_IO import Client
from flask import Flask, render_template, request

app = Flask(__name__)
aio = Client(username='arunshenoy99', key='aio_Ebjy37sK04hivec2zfrtUr99DiYL')


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/trigger', methods=['POST'])
def testing_trigger():
    requested_data = request.json
    data = aio.receive('testing')

    if data.value == requested_data['value']:
        return 'Worked'

    aio.send_data('testing', requested_data['value'])
    return 'Worked'


if __name__ == "__main__":
    app.run()
