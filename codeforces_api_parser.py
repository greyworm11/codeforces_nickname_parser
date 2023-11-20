import requests
import json

url = 'https://codeforces.com/api/user.ratedList'
response = requests.get(url)

items = json.loads(response.text)
file = open('codeforces_users.txt', 'w')

for item in items['result']:
	nick = item['handle']
	file.write(f'{nick}\n')