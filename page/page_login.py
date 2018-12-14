from base.base import *
import page


class Pagelogin(Base):

    def page_open(self):
        self.base_open_url()

    def page_input_username(self, username):
        self.base_send_keys(page.args_username, username)

    def page_input_password(self, password):
        self.base_send_keys(page.args_password, password)

    def page_input_verification(self, verification):
        self.base_send_keys(page.args_verification, verification)

    def page_click(self):
        self.base_click(page.args_login)
