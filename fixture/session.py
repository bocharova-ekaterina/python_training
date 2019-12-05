class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user_name, user_password):
        wd = self.app.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % user_name)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % user_password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()


