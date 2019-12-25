# -*- coding: utf-8 -*-
from model.client import Client


def test_client(app):
    old_clients = app.client.get_client_list()
    client = Client(firstname="Ekaterina", lastname="Bocharova", address="Shumakova, 23a",
                                      home="123456", mobile="987654321", work="456123", email="user1@mail.ru", email2="user2@mail.ru")
    app.client.add_client(client)
    new_clients=app.client.get_client_list()
    assert len(old_clients) + 1 == len(new_clients)
    old_clients.append(client)
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)


