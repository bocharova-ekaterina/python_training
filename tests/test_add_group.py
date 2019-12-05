# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(user_name="admin", user_password="secret")
    app.group.create(Group(name="test1", header="test1", footer="test1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(user_name="admin", user_password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
