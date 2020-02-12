from model.client import Client
import random

def test_edit_client(app, db, check_ui):
    client = Client(firstname="Ekaterina", lastname="Bocharova", address="Shumakova, 23a",
                                   home="123456", mobile="987654321", work="456123", email="user1@mail.ru", email2="user2@mail.ru")
    if app.client.count() == 0:
        app.client.add_client(client)
    old_clients = db.get_client_list()
    client_random = random.choice(old_clients)
    app.client.edit_client_by_id(client_random.id, Client(firstname="Irina"))
    assert len(old_clients) == app.client.count()
    new_clients = db.get_client_list()
    assert old_clients==new_clients
    if check_ui:
        assert sorted(new_clients, key=Client.id_or_max) == sorted(app.client.get_client_list(), key=Client.id_or_max)

