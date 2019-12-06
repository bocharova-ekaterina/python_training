

def test_del_client(app):
    app.session.login(user_name="admin", user_password="secret")
    app.client.del_first_clients()
    app.session.logout()
