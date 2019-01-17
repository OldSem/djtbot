import requests
import logging
import sys
import os
import asyncio
from asyncio import runners


token = '677828438:AAFTjrPEi3aRn41WobKa2H3Jc9F9wh2bWSU'
host = 'deb873ba.ngrok.io'
log = logging.getLogger('Django')
formatter = logging.Formatter(
    '%(asctime)s (%(filename)s:%(lineno)d %(threadName)s) %(levelname)s - %(name)s: "%(message)s"'
)
console_output_handler = logging.StreamHandler(sys.stderr)
console_output_handler.setFormatter(formatter)
log.addHandler(console_output_handler)
log.setLevel(logging.ERROR)
log.setLevel(logging.DEBUG)
log.setLevel(logging.INFO)


def cert():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cert = BASE_DIR + '/tgbot/bot.py'
    with open(cert, 'rb') as f:
        read = f.read()
        return read


def web_hook_info():
    r = requests.get(f'https://api.telegram.org/bot{token}/getWebhookInfo')
    if r.status_code != 200:
        log.error('Code: {0}; Text: {1}'.format(r.status_code, r.text))
    else:
        log.info('Code: {0}; Text: {1}'.format(r.status_code, r.text))


def delete_web_hook():
    r = requests.get(f'https://api.telegram.org/bot{token}/deleteWebhook')
    if r.status_code != 200:
        log.error('Code: {0}; Text: {1}'.format(r.status_code, r.text))
    else:
        log.info('Code: {0}; Text: {1}'.format(r.status_code, r.text))


def set_web_hook():
    r = requests.get(f'https://api.telegram.org/bot{token}/setWebhook', data={"url": host})
    if r.status_code != 200:
        log.error('Code: {0}; Text: {1}'.format(r.status_code, r.text))
    else:
        log.info('Code: {0}; Text: {1}'.format(r.status_code, r.text))


def get_me():
    r = requests.get(f'https://api.telegram.org/bot{token}/getMe')
    if r.status_code != 200:
        log.error('Code: {0}; Text: {1}'.format(r.status_code, r.text))
    else:
        log.info('Code: {0}; Text: {1}'.format(r.status_code, r.text))
    return r.text['id']


def send_message():
    r = requests.get(f'https://api.telegram.org/bot{token}/sendMessage', data={""})
    if r.status_code != 200:
        log.error('Code: {0}; Text: {1}'.format(r.status_code, r.text))
    else:
        log.info('Code: {0}; Text: {1}'.format(r.status_code, r.text))


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.close()


if __name__ == '__main__':
    runners.run(tcp_echo_client('Hello World!'))
