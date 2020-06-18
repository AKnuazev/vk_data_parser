import requests as r


def get_username(uid):
    user_params = {'v': 5.71,
                   'user_ids': uid,
                   'access_token': 'd9acf98cd9acf98cd9acf98c96d9de6273dd9acd9acf98c874aa57b9b6642522b5a44e4'}

    res = r.get('https://api.vk.com/method/users.get', params=user_params)
    print(res.json())

    first_name = str(res.json()['response'][0]['first_name'])
    last_name = str(res.json()['response'][0]['last_name'])
    uid = str(res.json()['response'][0]['id'])

    return first_name + ' ' + last_name + ' (id' + uid + ')'
