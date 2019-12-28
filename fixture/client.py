from model.client import Client


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

    def del_first_clients(self, index):
        wd = self.app.wd
        self.del_clients_by_index(0)

    def select_client_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

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

    def edit_client(self, new_client_data):
        wd = self.app.wd
        self.del_clients_by_index(0)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_client_list(self):
        if self.client_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.client_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                text = element.find_elements_by_css_selector("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = text
                firtname = text
                lastname = element.find_elements_by_tag_name("td")[1].text
                firtname = element.find_elements_by_tag_name("td")[2].text
                self.client_cache.append(Client(id=id, firstname=firtname, lastname=lastname))
            return list(self.client_cache)
