# -*- coding: utf-8 -*-
from model.client import Client
import string
import random
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10 #+ string.punctuation
    return prefix + " ".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


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

testdata = [Client(firstname="", lastname="", address="", home="", mobile="", work="", email="",email2="", email3="")] +[
            Client(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
            home=random_string("home", 10), mobile=random_string("mobile", 10), work=random_string("work", 10),
            email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("email3", 20))
            for i in range(3)]


@pytest.mark.parametrize("client", testdata, ids=[repr(x) for x in testdata])

def test_add_client(app, client):
    old_clients = app.client.get_client_list()
    app.client.add_client(client)
    assert len(old_clients) + 1 == app.client.count()
    new_clients = app.client.get_client_list()
    old_clients.append(client)
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)


