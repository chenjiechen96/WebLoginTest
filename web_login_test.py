import time
from selenium import webdriver

chromedriver = 'C:\\Program Files (x86)\\Google\\Chrome\Application\\chromedriver.exe'
url = 'https://ieeexplore.ieee.org/Xplore/home.jsp'
cki = '/html/body/div[1]/div/a'
login = '//*[@id="LayoutWrapper"]/div/div/div/div[1]/div[2]/ul/li[3]/a'
uname = '//*[@id="personal-sign-in"]/div[2]/form/div[1]/input'
pswd = '//*[@id="personal-sign-in"]/div[2]/form/div[2]/input'
iuname = '93601340@qq.com'
ipswd = 'abc12345'
sign_in = '//*[@id="personal-sign-in"]/div[2]/form/div[3]/button'
sign_out = '//*[@id="LayoutWrapper"]/div/div/div/div[1]/div[2]/ul/li[3]/a'
sign = '//*[@id="personal-sign-in"]/div[2]/div[1]/div[2]'
error = '//*[@id="personal-sign-in"]/div[2]/div[1]/div[2]'


def login_test():
    wb = webdriver.Chrome(chromedriver)
    wb.get(url)
    wb.maximize_window()
    wb.implicitly_wait(5)

    wb.find_element_by_xpath(cki).click()

    wb.find_element_by_xpath(login).click()

    ele_uname = wb.find_element_by_xpath(uname)
    ele_uname.clear()
    ele_uname.send_keys(iuname)

    ele_pswd = wb.find_element_by_xpath(pswd)
    ele_pswd.clear()
    ele_pswd.send_keys(ipswd)

    wb.find_element_by_xpath(sign_in).click()
    time.sleep(5)

    ele_err = wb.find_element_by_xpath(error)

    if ele_err.text == '':
        print('OK')
    else:
        print('hoops')

    time.sleep(5)
    wb.quit()


if __name__ == '__main__':
    login_test()
