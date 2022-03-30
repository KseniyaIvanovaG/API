import requests
import json
from pprint import pprint
# В документации прописано, что для просмотра реппозиториев пользователя,
# необходимо получить данные по ссылке https://api.github.com/users/octocat/repos,
# где octocat - это имя пользователя
# Я просмотрю список своих реппозитриев
url = 'https://api.github.com/users/'
user = 'KseniyaIvanovaG'
# Запросим данные используя ссылку и имя пользователя
response = requests.get(f'{url}{user}/repos')
# Сохраним данные в переменную
j_data = response.json()
pprint(j_data)
# Сохраним данные в файл json
with open('data.json', 'w') as outfile:
    json.dump(j_data, outfile)
# Выведем на экран наименования реппозиториев
for r in j_data:
    print('Name: ' + r['name'])