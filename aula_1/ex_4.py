import requests

URL = 'https://gen-net.herokuapp.com/api/users/{}'

#response = requests.get(URL)
#print(response.json()) 


#usremail = input('Digite seu email: ')
#print(usremail)

#URL_FORMATADA = URL.format(usremail)
#print(URL_FORMATADA)

#response = requests.get(URL_FORMATADA)

#print(response)


 
res = requests.get(URL)


users = res.json()

email = input('Digite seu email: ')



for user in users:
		if user.get('email') == email:
				print(users)

