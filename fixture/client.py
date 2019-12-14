
class ClientHelper:

    def __init__(self, app):
        self.app = app

    def add_client(self, client):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_client_form(client)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_home_page()

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

    def del_first_clients(self):
        wd = self.app.wd
       # wd.find_element_by_id("MassCB").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_client(self, new_client_data):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_client_form(new_client_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def count(self):
        self.app.open_home_page()
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))


