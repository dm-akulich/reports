import requests


# headers = {'Authorization': 'Token 28db9a3c44bb37307afcbccea4276b0dfd7d3893',}


def api_autorization():
    while True:
        f = open("api_key.txt", "r")
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
