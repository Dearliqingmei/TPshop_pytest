import sys
import os

sys.path.append(os.getcwd())

import time
from page.page_login import *
from page.page_mymall import *
from page.page_in import *
import pytest
import scripts
from base.read_logindata_yaml import *
import allure


def get_data():
    data_list = list()
    get_data_yaml = Readlogindatayaml("data_login.yaml").read_logindata_yaml()
    for data_login in get_data_yaml.values():
        data_list.append((data_login["username"], data_login["password"], data_login["verification"]))
    return data_list


class Testlogin():

    def setup(self):
        self.testlogin = PageIn().page_get_pagelogin(scripts.driver, scripts.url_login)
        self.testlogin.page_open()

    def teardown(self):
        self.testlogin.driver.quit()

    @pytest.mark.parametrize("username,password,verification", get_data())
    # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    # @allure.step('登陆测试')
    def test_login(self, username, password, verification):
        self.testlogin.page_input_username(username)
        self.testlogin.page_input_password(password)
        self.testlogin.page_input_verification(verification)
        self.testlogin.page_click()
        time.sleep(10)
        self.testhomepage = PageIn().page_get_pagemymall(scripts.driver, scripts.url_homepage)
        # 断言
        try:
            assert self.testhomepage.pagehomepage_show_username(username)
            print("登录成功！")
            self.testhomepage.base_screenhot()
        except:
            print("登录失败！")
            self.testlogin.base_screenhot()
