import pymysql.cursors
from model.group import Group
from model.client import Client


class dBFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        list =[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer)= row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_client_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook where deprecated ='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                list.append(Client(id=str(id), firstname=firstname, lastname=lastname, address=address, home=home, mobile=mobile,
                                   work=work, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def get_clients_from_group(self, group_id):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute(
                "select id, group_id from address_in_groups where group_id=?", str(group_id))
            row = cursor.fetchone()
            list.append(row)
            #for row in cursor:
                #(id, group_id)=row
                #list.append(str(id), str(group_id))
        finally:
            cursor.close()
        return list