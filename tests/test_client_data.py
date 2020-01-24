from random import randrange
import re
from fixture.db import dBFixture
from model.client import Client



def test_client_phones_from_home_page(app):
    client_from_home_page = app.client.get_client_list()[0]
    client_from_edit_home_page = app.client.get_client_info_from_edit_page(0)
    assert client_from_home_page.all_phones_from_home_page == merge_phones_on_home_page(client_from_edit_home_page)


def test_client_phones_from_view_page(app):
    client_from_view_page = app.client.get_client_from_view_page(0)
    client_from_edit_home_page = app.client.get_client_info_from_edit_page(0)
    assert client_from_view_page.home == client_from_edit_home_page.home
    assert client_from_view_page.work == client_from_edit_home_page.work
    assert client_from_view_page.mobile == client_from_edit_home_page.mobile
    assert client_from_view_page.phone2 == client_from_edit_home_page.phone2


def test_client_data_on_home_page(app):
    client_from_home_page = app.client.get_client_list()
    index = randrange(len(client_from_home_page))
    client_from_home_page_random = client_from_home_page[index]
    client_from_edit_page = app.client.get_client_info_from_edit_page(index)
    assert client_from_home_page_random.firstname == client_from_edit_page.firstname
    assert client_from_home_page_random.lastname == client_from_edit_page.lastname
    assert client_from_home_page_random.address == client_from_edit_page.address
    assert client_from_home_page_random.all_phones_from_home_page == merge_phones_on_home_page(client_from_edit_page)
    assert client_from_home_page_random.all_emails_from_home_page == merge_emails_on_home_page(client_from_edit_page)


def test_client_data_on_db(app, db):
    clients_from_ui = sorted(app.client.get_client_list(), key=Client.id_or_max)
    clients_from_db = sorted(db.get_client_list(), key=Client.id_or_max)
    for i,  clients in enumerate(clients_from_ui):
        client_from_db = clients_from_db[i]
        assert clients.firstname == client_from_db.firstname
        assert clients.lastname == client_from_db.lastname
        assert clients.address == client_from_db.address
        assert clients.all_phones_from_home_page == merge_phones_on_home_page(client_from_db)
        assert clients.all_emails_from_home_page == merge_emails_on_home_page(client_from_db)


def clear(s):
    return re.sub("[() \n -]", "", s)

def merge_phones_on_home_page(client):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x:clear(x),
                                filter(lambda x: x is not None,
                                       [client.home, client.mobile, client.work, client.phone2]))))


def merge_emails_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",[contact.email, contact.email2, contact.email3]))