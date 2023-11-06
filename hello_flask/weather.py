import urllib.request
import json


# print(url)

def get_temperature(city):
    
    APIKEY = '7cb24f95fbf2512e936a2834ab896b2b'
    city = 'Wellesley'
    country_code = 'us'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data['main']['temp']
    
if __name__ == '__main__':
    city = input('Enter: ')
    print(get_temperature(city))

