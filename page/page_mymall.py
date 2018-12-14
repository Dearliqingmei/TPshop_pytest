from  base.base import *
import page

class Pagehomepage(Base):

    def pagehomepage_show_username(self,username):
        return self.base_show_username(page.args_loginname) in username

    def pagehomepage_click_homepage(self):
        self.base_click(page.args_homepage)