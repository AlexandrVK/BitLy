import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def shorten_link(token, user_input):

    url = "https://api-ssl.bitly.com/v4/bitlinks"
    payload = {"long_url": user_input}
    header = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, headers = header, json = payload)
    response.raise_for_status()
  
    return response.json()['link']


def count_clicks(token, user_input):

    url = f"https://api-ssl.bitly.com/v4/bitlinks/{user_input}/clicks/summary"
    header = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers = header)
    response.raise_for_status()
  
    return response.json()['total_clicks']


def is_bitlink(token, user_input):
    temp_parsed_user_input = urlparse(user_input)
    parsed_user_input = temp_parsed_user_input.path if not temp_parsed_user_input.netloc else f"{temp_parsed_user_input.netloc}{temp_parsed_user_input.path}"
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_user_input}"
    header = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers = header)
    
    return response.ok


if __name__ == '__main__':
    
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    
    
    parser = argparse.ArgumentParser(
        description='Прорамма обработки ссылок для сайта Bit.ly'
    )
    parser.add_argument('user_input', help='Введите ссылку:')
    args = parser.parse_args()
        
    try:
        if is_bitlink(token, args.user_input):
            temp_parsed_user_input = urlparse(args.user_input)
            bitlink = temp_parsed_user_input.path if not temp_parsed_user_input.netloc else f"{temp_parsed_user_input.netloc}{temp_parsed_user_input.path}"
            click_sum = count_clicks(token,bitlink)
            print(f"По вашей ссылке прошли {click_sum} раз(а)")
        else:  
            bitlink = shorten_link(token, args.user_input)
            print('Битлинк:', bitlink)
        
    except requests.exceptions.HTTPError:
        print('Ошибка: Неверная ссылка')
        
