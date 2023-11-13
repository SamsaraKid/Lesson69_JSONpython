import requests

key = 'f1bbc900ee2e50dc66bebd83f2f0a9f3'
site = 'https://api.openweathermap.org/data/2.5/weather'
id = 524901

try:
    res = requests.get(site, params={'id': id, 'appid': key, 'lang': 'ru', 'units': 'metric'})
    print(res.json())
    data = res.json()
    k1 = data.get('name')
    k2 = str(round(data['main']['temp'], 1)) + 'C'
    k3 = str(data['wind']['speed']) + 'м/с'
    k4 = data['weather'][0]['description']
    print(k1, k2, k3, k4)
except Exception as e:
    print(e)

print('########################################################')

site = 'https://api.openweathermap.org/data/2.5/forecast'
res = requests.get(site, params={'id': id, 'appid': key, 'lang': 'ru', 'units': 'metric'})
print(res.json())
data = res.json()
for i in data['list']:
    if i['dt_txt'][11:13] == '15':
        print(i['dt_txt'], i['main']['temp'], i['weather'][0]['description'])

print('########################################################')

import requests

url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

headers = {
    "accept": "application/json",
    "X-RapidAPI-Key": "e062a2139emsh6813df0aa6d3a8ep1b07ccjsn63c695a123d2",
    "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

joke = response.json()['value']
print(joke)

# url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
#
# payload = {
# 	"source": "en",
# 	"target": "ru",
# 	"q": joke
# }
# headers = {
# 	"content-type": "application/x-www-form-urlencoded",
# 	"Accept-Encoding": "application/gzip",
# 	"X-RapidAPI-Key": "e062a2139emsh6813df0aa6d3a8ep1b07ccjsn63c695a123d2",
# 	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
# }
#
# response = requests.post(url, data=payload, headers=headers)
#
# print(response.json()['data']['translations'][0]['translatedText'])

print('########################################################')

url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
    "X-RapidAPI-Key": "e062a2139emsh6813df0aa6d3a8ep1b07ccjsn63c695a123d2",
    "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}

response_films = requests.get(url, headers=headers)

films = response_films.json()
print('=====Top 100 movies=====')
for f in films:
    print(str(f['rank']) + '. ' + f['title'])
