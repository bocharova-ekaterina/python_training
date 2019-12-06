from model.client import Client


def test_client(app):
    app.session.login(user_name="admin", user_password="secret")
    app.client.edit_client(Client(firstname="Irina"))
    app.session.logout()