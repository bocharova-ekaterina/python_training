# -*- coding: utf-8 -*-
from models.client import Client
from fixture.fixture import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_client(app):
    app.open_home_page()
    app.session.login(user_name="admin", user_password="secret")
    app.client.add_client(Client(firstname="Bocharova", lastname="Ekaterina", address="Shumakova, 23a",
                                      home_phone="123456", mobile_phone="987654321", work_phone="456123",
                                      email_1="user1@mail.ru", email_2="user2@mail.ru"))
    app.session.logout()

