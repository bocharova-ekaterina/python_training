from model.client import Client
from random import randrange


def test_edit_client(app):
    old_clients = app.client.get_client_list()
    client = Client(firstname="Ekaterina", lastname="Bocharova", address="Shumakova, 23a",
                                   home="123456", mobile="987654321", work="456123", email="user1@mail.ru", email2="user2@mail.ru")
    index = randrange(len(old_clients))
    client.id = old_clients[index].id
    if app.client.count() == 0:
        app.client.add_client()
    app.client.edit_client_by_index(index, Client(firstname="Irina"))
    assert len(old_clients) == app.client.count()
    new_clients = app.client.get_client_list()
    old_clients[index] = client
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)
