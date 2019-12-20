# -*- coding: utf-8 -*-
from model.client import Client


def test_client(app):
    old_clients = app.client.get_client_list()
    app.client.add_client(Client(firstname="Ekaterina", lastname="Bocharova", address="Shumakova, 23a",
                                      home="123456", mobile="987654321", work="456123", email="user1@mail.ru", email2="user2@mail.ru"))
    new_clients=app.client.get_client_list()
    assert len(old_clients) + 1 == len(new_clients)


