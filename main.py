import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, user_input):

    url = "https://api-ssl.bitly.com/v4/bitlinks"
    payload = {"long_url": user_input}
    header = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=header, json=payload)
    response.raise_for_status()

    return response.json()['link']


def count_clicks(token, user_input):

    url = f"https://api-ssl.bitly.com/v4/bitlinks/{user_input}/clicks/summary"
    header = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=header)
    response.raise_for_status()

    return response.json()['total_clicks']


def is_bitlink(token, user_input):
    parsed_url = urlparse(user_input)
    parsed_user_input = f"{parsed_url.netloc}{parsed_url.path}"
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_user_input}"
    header = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=header)

    return response.ok


if __name__ == '__main__':

    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    user_input = input('Введите ссылку:')

    try:
        if is_bitlink(token, user_input):
            parsed_url = urlparse(user_input)
            bitlink = f"{parsed_url.netloc}{parsed_url.path}"
            click_sum = count_clicks(token, bitlink)
            print(f"По вашей ссылке прошли {click_sum} раз(а)")
        else:
            bitlink = shorten_link(token, user_input)
            print('Битлинк:', bitlink)

    except requests.exceptions.HTTPError:
        print('Ошибка: Неверная ссылка')
