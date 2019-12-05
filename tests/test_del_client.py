

def test_del_client(app):
    app.session.login(user_name="admin", user_password="secret")
    app.client.del_all_clients()
    app.session.logout()
