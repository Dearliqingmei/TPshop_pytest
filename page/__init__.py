from selenium.webdriver.common.by import By

#登录
args_username=By.ID,"username"
args_password=By.ID,"password"
args_verification=By.ID,"verify_code"
args_login=By.CSS_SELECTOR,"#loginform > div > div.login_bnt > a"


#跳转我的商城
args_loginname=By.CSS_SELECTOR,"body > div.tpshop-tm-hander.home-index-top.p > div > div > div > div.fl.islogin.hide > a.red.userinfo"
args_homepage=By.CSS_SELECTOR,"body > div.nav-middan-z.p.home-index-head > div > div.m-navitems > ul > li:nth-child(1) > a"
