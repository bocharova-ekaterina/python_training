# -*- coding: utf-8 -*-
from model.client import Client


def test_client(app):
    old_clients = app.client.get_client_list()
    client = Client(firstname="Ekaterina", lastname="Bocharova", address="Shumakova, 23a",
                                      homephone="123456", mobilephone="987654321", workphone="456123", email="user1@mail.ru", email2="user2@mail.ru")
    app.client.add_client(client)
    assert len(old_clients) + 1 == app.client.count()
    new_clients = app.client.get_client_list()
    old_clients.append(client)
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)


