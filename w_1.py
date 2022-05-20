from os import makedirs
from os.path import join
import requests
from concurrent.futures import ThreadPoolExecutor


def get_user():
    return requests.get('https://randomuser.me/api/')


def get_cat():
    return requests.get('https://catfact.ninja/fact')


def handle(num):
    user = get_user()
    cat = get_cat()

    dir = join(f'user_data/{num}')
    makedirs(dir)
    with open(join(dir, 'user_info.txt'), 'w', encoding='utf-8') as f:
        f.write(user.text)
    with open(join(dir, 'cat_fact.txt'), 'w', encoding='utf-8') as f:
        f.write(cat.json()['fact'])

    picture_url = user.json()['results'][0]['picture']['large']
    with open(join(dir, picture_url.split('/')[-1]), 'wb') as f:
        r = requests.get(picture_url)
        f.write(r.content)


with ThreadPoolExecutor(4) as pool:
    pool.map(handle, (i for i in range(1, 13)))
