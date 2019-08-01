import requests

URL = 'https://viacep.com.br/ws/{}/json'


cep = input('Digite seu cep: ')
print(cep)

URL_FORMATADA = URL.format(cep)
print(URL_FORMATADA)

response = requests.get(URL_FORMATADA)

print(response)
print(dir(response))

x = response.json()
print(type(x))