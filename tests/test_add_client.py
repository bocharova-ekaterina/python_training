# -*- coding: utf-8 -*-
from model.client import Client
from generator.client import testdata
import pytest


#testdata=[
        #Client(firstname=firstname, lastname=lastname, address=address, home=home, mobile=mobile, work=work, email=email, email2=email2)
        #for firstname in [random_string("firstname", 10)]
        #for lastname in [" ", random_string("lastname", 10)]
        #for address in [" ", random_string("address", 20)]
        #for home in [" ", random_string("home", 10)]
        #for mobile in [" ", random_string("mobile", 10)]
        #for work in [" ", random_string("work", 10)]
        #for email in [" ", random_string("email", 20)]
        #for email2 in [" ", random_string("email2", 20)]]


@pytest.mark.parametrize("client", testdata, ids=[repr(x) for x in testdata])

def test_add_client(app, client):
    old_clients = app.client.get_client_list()
    app.client.add_client(client)
    assert len(old_clients) + 1 == app.client.count()
    new_clients = app.client.get_client_list()
    old_clients.append(client)
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)


