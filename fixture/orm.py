from pony.orm import *
from datetime import datetime
from model.group import Group
from model.client import Client
from pymysql.converters import decoders

class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        clients = Set(lambda:ORMFixture.ORMClient, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMClient(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda:ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="clients", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()


    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_clients_to_model(self, clients):
        def convert(client):
            return Client(id=str(client.id), firstname=client.firstname, lastname=client.lastname)
        return list(map(convert, clients))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select (g for g in ORMFixture.ORMGroup))

    @db_session
    def get_client_list(self):
        return self.convert_clients_to_model(select(c for c in ORMFixture.ORMClient if c.deprecated is None))

    @db_session
    def get_client_in_group(self, group):
        orm_group = list(select (g for g in ORMFixture.ORMGroup if g.id==group.id))[0]
        return self.convert_clients_to_model(orm_group.clients)

    @db_session
    def get_client_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_clients_to_model(select (c for c in ORMFixture.ORMClient if c.deprecated not in c.groups))

