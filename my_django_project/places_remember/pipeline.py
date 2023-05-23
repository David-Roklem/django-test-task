import logging

import requests

from .models import Userpic


def choose_picture(vk_response):
    print(vk_response)
    if (vk_response['count'] == 0):
        return None
    result = None
    for size in vk_response['items'][0]['sizes']:
        if size['type'] == 'y':
            result = size['url']

    return result


def store_userpic(
        backend, strategy, details, response, user=None, *args, **kwargs):
    if not user:
        return

    if Userpic.objects.filter(username=user).count() > 0:
        return

    user_id = response['user_id']
    token = response['access_token']
    url = 'https://api.vk.com/method/photos.get?access_token={}&v=5.131&owner_id={}&album_id=profile'.format(token, user_id)
    picture = response.get('user_photo')
    try:
        vk_response = requests.get(url).json()['response']
        vk_pic = choose_picture(vk_response)
        if vk_pic:
            picture = vk_pic
    except Exception as e:
        logging.exception(e)

    if picture:
        userpic = Userpic()
        userpic.username = user
        userpic.pic = picture
        userpic.save()
