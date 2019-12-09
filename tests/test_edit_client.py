from model.client import Client


def test_client(app):
    app.client.edit_client(Client(firstname="Irina"))
