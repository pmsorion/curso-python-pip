import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    # convertimosla respuesta de request de string a un json
    categories = r.json()

    # de esta forma podemos iterar dentro de las categories y ver uno a uno
    for category in categories:
        print(category['name'])