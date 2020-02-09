from model.client import Client
import random
import allure

def test_del_client(app, db, check_ui):
    with allure.step('Given a group list'):
        if len(db.get_group_list()) == 0:
            app.client.add_client(Client(firstname="Ekaterina", lastname="Bocharova", address="Shumakova, 23a",
                                      home="123456", mobile="987654321", work="456123", email="user1@mail.ru", email2="user2@mail.ru"))
        old_clients = db.get_client_list()
        client = random.choice(old_clients)
    with allure.step('When I delete a client %s to the list' % client):
        app.client.del_client_by_id(client.id)
    with allure.step('Then the new client list is less to the old list without the deleted client'):
        assert len(old_clients) - 1 == app.client.count()
        old_clients.remove(client)
        new_clients = db.get_client_list()
        assert old_clients == new_clients
        if check_ui:
            assert sorted(new_clients, key=Client.id_or_max) == sorted(app.client.get_client_list(), key=Client.id_or_max)



