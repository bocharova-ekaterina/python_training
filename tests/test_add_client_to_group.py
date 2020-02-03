import random
from model.group import Group
from model.client import Client


def test_add_client_to_group(app, db, orm):
    #выполняем предусловия
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1", header="test1", footer="test1"))
    if len(db.get_client_list()) == 0:
        app.client.add_client(Client(firstname="Ekaterina", lastname="Bocharova", address="Shumakova, 23a"))
    #выбираем рандомную группу
    old_groups = app.group.get_group_list()
    random_group = random.choice(old_groups)
    group_db_id = random_group.id
    #выбираем рандомного клиента не состоящего в группе
    client_at_not_group = orm.get_client_not_in_group(random_group)
    random_client = random.choice(client_at_not_group)
    old_clients_from_group=db.get_clients_from_group(group_db_id)
    app.client.add_client_to_group(random_client, random_group)
    new_clients_from_group=db.get_clients_from_group(group_db_id)
    assert len(old_clients_from_group)==len(new_clients_from_group)+1




