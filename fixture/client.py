from model.client import Client
import re


class ClientHelper:

    client_cache = None

    def __init__(self, app):
        self.app = app

    def add_client(self, client):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_client_form(client)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_home_page()
        self.client_cache = None

    def fill_client_form(self, client):
        wd = self.app.wd
        self.change_field_value("firstname", client.firstname)
        self.change_field_value("lastname", client.lastname)
        self.change_field_value("address", client.address)
        self.change_field_value("home", client.home)
        self.change_field_value("mobile", client.mobile)
        self.change_field_value("work", client.work)
        self.change_field_value("phone2", client.phone2)
        self.change_field_value("email", client.email)
        self.change_field_value("email2", client.email2)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_clients_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_client_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.client_cache = None

    def del_client_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_client_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.client_cache = None

    def del_first_clients(self, index):
        wd = self.app.wd
        self.del_clients_by_index(0)

    def select_client_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_client_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_client_by_name(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_client_by_index(self, index, new_client_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_client_form(new_client_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.client_cache = None

    def edit_client_by_id(self, id, new_client_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_client_by_id(id)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_client_form(new_client_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.client_cache = None

    def edit_client(self, new_client_data):
        wd = self.app.wd
        self.edit_client_by_index(0)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_client_list(self):
        if self.client_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.client_cache = []
            for row in wd.find_elements_by_css_selector("tr[name=entry]"):
                cells = row.find_elements_by_css_selector("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firtname = cells[2].text
                all_phones=cells[5].text
                all_emails=cells[4].text
                address=cells[3].text
                self.client_cache.append(Client(id=id, firstname=firtname, lastname=lastname, address=address, all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
            return list(self.client_cache)

    def open_client_to_edit(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_client_to_view(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row=wd.find_elements_by_name("entry")[index]
        cell=row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_client_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_client_to_edit(index)
        firstname=wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        firstemail = wd.find_element_by_name("email").get_attribute("value")
        secondemail = wd.find_element_by_name("email2").get_attribute("value")
        thirdemail = wd.find_element_by_name("email3").get_attribute("value")
        address=wd.find_element_by_name("address").get_attribute("value")
        return Client(firstname=firstname, lastname=lastname, id=id,
                      home=homephone, work=workphone, mobile=mobilephone, phone2=secondaryphone,
                      email=firstemail, email2=secondemail, email3=thirdemail, address=address)

    def get_client_from_view_page(self, index):
        wd = self.app.wd
        self.open_client_to_view(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Client(home=homephone, work=workphone,  mobile=mobilephone, phone2=phone2)

    def add_client_to_group(self, client_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_client_by_id(client_id)
        wd.find_element_by_name("to_group").click()
        self.choice_group_by_id(group_id)
        wd.find_element_by_name("add").click()
        self.app.open_home_page()

    def choice_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("option[value='%s']" % id).click()

    def del_client_from_group(self, client_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("option[value='%s']" % id).click()
        self.select_client_by_id(client_id)
        wd.find_element_by_name("remove").click()
        self.app.open_home_page()





