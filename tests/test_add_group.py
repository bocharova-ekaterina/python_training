# -*- coding: utf-8 -*-
from model.group import Group
from fixture.fixture import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.session.login(user_name="admin", user_password="secret")
    app.group.create(Group(name="test1", header="test1", footer="test1"))
    app.session.logout()


def test_add_empty_group(app):
    app.open_home_page()
    app.session.login(user_name="admin", user_password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
