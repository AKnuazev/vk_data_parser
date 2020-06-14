import requests as r


def calc_age(uid):
    token = 'd9acf98cd9acf98cd9acf98c96d9de6273dd9acd9acf98c874aa57b9b6642522b5a44e4'
    version = 5.71
    parameters = {'v': version, 'user_id': uid, 'access_token': token}
    parameters2 = {'v': version, 'user_id': uid, 'access_token': token, 'fields': 'bdate'}

    res = r.get('https://api.vk.com/method/users.get', params=parameters)
    res2 = r.get('https://api.vk.com/method/friends.get', params=parameters2)
    print(res.text)
    print(res2.text)
    print()
    return res.text, res2.text


if __name__ == '__main__':
    res = calc_age(190662692)
    print(res)
