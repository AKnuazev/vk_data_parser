import requests as r
from datetime import datetime


def add_to_list(res_list, age):
    found = False

    for cort in res_list:
        if cort[0] == age:
            cort[1] += 1
            found = True
            break

    if not found:
        res_list.append([age, 1])


def parce_friends(res_json):
    res_list = []
    for i in range(res_json['response']['count']):
        if 'bdate' in res_json['response']['items'][i]:
            bdate = res_json['response']['items'][i]['bdate']
            if len(bdate) > 5:
                dot_pos = bdate.rfind('.')
                byear = int(bdate[dot_pos + 1:])
                age = datetime.now().year - byear

                add_to_list(res_list, age)

    return res_list


def sort_list(res_list):
    res_list.sort(key=lambda pair: pair[0])
    res_list.sort(key=lambda pair: pair[1], reverse=True)


def convert_list(res_list):
    new_list = []
    for pair in res_list:
        new_list.append((pair[0], pair[1]))

    return new_list


def calc_age(uid):
    # access_token = 4a3358b3f7b982989454757c924cc54ae8070eb1b40488cad710b320daa5a8c62fdcfde23ca1921feb58a

    user_params = {'v': 5.126,
                   'user_ids': uid,
                   'access_token': 'd9acf98cd9acf98cd9acf98c96d9de6273dd9acd9acf98c874aa57b9b6642522b5a44e4'}

    res = r.get('https://api.vk.com/method/users.get', params=user_params)
    uid = res.json()['response'][0]['id']

    friends_params = {'v': 5.126,
                      'user_id': uid,
                      'access_token': 'd9acf98cd9acf98cd9acf98c96d9de6273dd9acd9acf98c874aa57b9b6642522b5a44e4',
                      'fields': 'bdate'}

    res = r.get('https://api.vk.com/method/friends.get', params=friends_params)

    res_list = parce_friends(res.json())
    sort_list(res_list)
    res_list = convert_list(res_list)

    return res_list


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
