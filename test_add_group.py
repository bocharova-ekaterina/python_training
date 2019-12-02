# -*- coding: utf-8 -*-
from group import Group
from fixture import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.login(user_name="admin", user_password="secret")
    app.create_new_group(Group(name="test1", header="test1", footer="test1"))
    app.logout()


def test_add_empty_group(app):
    app.open_home_page()
    app.login(user_name="admin", user_password="secret")
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()
