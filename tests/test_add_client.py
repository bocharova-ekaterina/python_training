# -*- coding: utf-8 -*-
from model.client import Client


def test_client(app):
    app.client.add_client(Client(firstname="Ekaterina", lastname="Bocharova", address="Shumakova, 23a",
                                      home="123456", mobile="987654321", work="456123", email1="user@mail.ru", email2="u@mail.ru"))


