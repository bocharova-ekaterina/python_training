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
    group = random.choice(old_groups)
    #выбираем рандомного клиента не состоящего в группе
    client_at_not_group = orm.get_client_not_in_group(group)
    add_client_to_group = app.client.add_client_to_group(client_at_not_group, group)
    assert add_client_to_group in orm.get_client_in_group(group)




