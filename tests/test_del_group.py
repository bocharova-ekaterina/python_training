
def test_del_first_group(app):
    app.session.login(user_name="admin", user_password="secret")
    app.group.del_first_group()
    app.session.logout()