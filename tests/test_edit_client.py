from model.client import Client


def test_client(app):
    if app.client.count() == 0:
        app.client.add_client(Client(firstname="Ekaterina", lastname="Bocharova", address="Shumakova, 23a",
                                     home="123456", mobile="987654321", work="456123", email="user1@mail.ru",
                                     email2="user2@mail.ru"))
        app.fixture.open_home_page()
    app.client.edit_client(Client(firstname="Irina"))
