# -*- coding: utf-8 -*-
from model.client import Client


def test_add_client(app, json_clients, db, check_ui):
    client=json_clients
    old_clients = db.get_client_list()
    app.client.add_client(client)
    assert len(old_clients) + 1 == app.client.count()
    new_clients = db.get_client_list()
    old_clients.append(client)
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)
    if check_ui:
        assert sorted(new_clients, key=Client.id_or_max) == sorted(app.group.get_group_list(), key=Client.id_or_max)


