from model.client import Client


def test_del_client(app):
    if app.client.count() == 0:
        app.client.add_client(Client(firstname="Ekaterina", lastname="Bocharova", address="Shumakova, 23a",
                                      home="123456", mobile="987654321", work="456123", email="user1@mail.ru", email2="user2@mail.ru"))
    old_clients = app.client.get_client_list()
    app.client.del_first_clients()
    new_clients = app.client.get_client_list()
    assert len(old_clients) - 1 == len(new_clients)
    old_clients[0:1] = []
    assert old_clients == new_clients



