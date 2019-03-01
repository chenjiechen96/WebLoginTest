import time
from selenium import webdriver

chromedriver = 'C:\\Program Files (x86)\\Google\\Chrome\Application\\chromedriver.exe'
url = 'https://ieeexplore.ieee.org/Xplore/home.jsp'
ele_info = {'Login_xpath': '//*[@id="LayoutWrapper"]/div/div/div/div[1]/div[2]/ul/li[3]/a',
            'Acc_xpath': '//*[@id="personal-sign-in"]/div[2]/form/div[1]/input',
            'Pwd_xpath': '//*[@id="personal-sign-in"]/div[2]/form/div[2]/input',
            'Sign_xpath': '//*[@id="personal-sign-in"]/div[2]/form/div[3]/button'}
account = {'Username': '93601340@qq.com', 'Password': 'abc12345'}
sign_out = '//*[@id="LayoutWrapper"]/div/div/div/div[1]/div[2]/ul/li[3]/a'
error = '//*[@id="personal-sign-in"]/div[2]/div[1]/div[2]'


def open_browser():
    webdriver_handle = webdriver.Chrome(chromedriver)
    return webdriver_handle


def open_url(handle, address):
    handle.get(address)
    handle.maximize_window()


def find_elements(d, arg):
    d.find_element_by_xpath(arg['Login_xpath']).click()
    ele_acc = d.find_element_by_xpath(arg['Acc_xpath'])
    ele_pwd = d.find_element_by_xpath(arg['Pwd_xpath'])
    ele_sign = d.find_element_by_xpath(arg['Sign_xpath'])
    return ele_acc, ele_pwd, ele_sign


def send_values(eletuple, arg):
    listkey = ['Username', 'Password']
    for i, key in enumerate(listkey):
        eletuple[i].clear()
        eletuple[i].send_keys(arg[key])
    eletuple[2].click()


def check_results(d, err_id):
    ele_err = d.find_element_by_xpath(err_id)
    if ele_err.text == '':
        print('Pass')
    else:
        print(ele_err.text)


def login_test():
    wd = open_browser()
    open_url(wd, url)

    wd.implicitly_wait(5)

    ele_tuple = find_elements(wd, ele_info)
    send_values(ele_tuple, account)

    time.sleep(5)

    check_results(wd, error)

    time.sleep(3)

    wd.quit()


if __name__ == '__main__':
    login_test()
