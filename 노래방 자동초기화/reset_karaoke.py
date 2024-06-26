import requests

url = 'https://kmlaonline.net/proc/util/karaoke'

session = requests.Session()
response = session.get('https://kmlaonline.net/')
cookies = response.cookies

params = {
  'util_action': 'clear_week'
}

res= requests.post(url, params=params)

if res.status_code == 200:
  print('Succesfully reset karaoke')
else:
  print('Failed to reset karaoke', res.status_code, res.text)