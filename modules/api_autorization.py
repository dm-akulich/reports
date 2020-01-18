# - *- coding: utf- 8 - *-

import requests

def api_autorization():
    while True:
        f = open(".api_key", "r")
        f = f.read()
        headers = {}
        headers['Authorization'] = 'Token ' + f

        server_response = requests.get('https://api4.seranking.com/account/balance', headers=headers)
        server_response = str(server_response)
        if server_response == '<Response [200]>':
            print('Авторизация прошла успешно')
            input('Нажиме ENTER, чтобы продолжить.')
            break
        else:
            x = input('Ошибка авторизации. Нажмите Ctrl+C, чтобы закрыть программу.')

    return headers
