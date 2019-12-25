from model.client import Client


def test_client(app):
    old_clients = app.client.get_client_list()
    client=Client(firstname="Ekaterina", lastname="Bocharova", address="Shumakova, 23a",
                                      home="123456", mobile="987654321", work="456123", email="user1@mail.ru", email2="user2@mail.ru")
    client.id = old_clients[0].id
    if app.client.count() == 0:
        app.client.add_client()
    app.client.edit_client(Client(firstname="Irina"))
    new_clients = app.client.get_client_list()
    assert len(old_clients) == len(new_clients)
    old_clients[0] = client
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)
