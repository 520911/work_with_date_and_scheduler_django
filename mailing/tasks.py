import os
import time

import requests

from mailing.models import Mailing, Client, Request


def post_request(ids,
                 url=os.environ.get('URL', default='https://probe.fbrq.cloud/v1/send/'),
                 token=os.environ.get('JWT',
                                      default='eyJhbGciO5cCI6IkpXVCJ9.'
                                              'eyJleHAiOjmZhYnJpcXVlIiwibmFtZSI6IkRlbmlzIn0.'
                                              'koFNsnOlaM9L0vbAbwDeuaReHURjg')):
    header = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'}
    mailing = Mailing.objects.filter(id=ids).first()
    clients = Client.objects.filter(mobile_code=mailing.mobile_code).all()
    for client in clients:
        messages = Request.objects.filter(client_id=client.id,
                                          status='NEW').select_related('client', 'mailing').all()

        for message in messages:
            data = {
                'id': message.id,
                "phone": client.phone,
                "text": mailing.text
            }
            count = 0
            try:
                response = requests.post(url=url + str(message.id), headers=header, json=data)
                print(response.status_code)
                while response.status_code != 200 and count < 200:
                    time.sleep(2)
                    count += 1
            except ConnectionError:
                return f'Server dos"t exists'


