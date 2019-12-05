from model.group import Group


def test_del_first_group(app):
    app.session.login(user_name="admin", user_password="secret")
    app.group.edit_first_group(Group(name="updated group", header="updated group", footer="updated group"))
    app.session.logout()