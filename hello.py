from flask import Flask,request,jsonify
import requests,numpy

app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'])

def index():
    data = request.get_json()
    city = data['queryResult']['parameters']['geo-city'][0]
    # print(city)
    cf = conversion_factor(city)
    celtemp = cf - 273.0
    final_temp = numpy.round(celtemp,2)
    # print(final_temp)
    response = {
        'fulfillmentText': f'Current temperature in {city} is {final_temp} degree celcius '
    }
    return jsonify(response)

def conversion_factor(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3c708ff25702160194aa89a190fbb05b"
    response = requests.get(url)
    response = response.json()
    response = response['main']['temp']
    # print(response)
    return response

if __name__ == "__main__":
    app.run(debug=True)