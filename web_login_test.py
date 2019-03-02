import time
from selenium import webdriver
from UserData import Webinfo, Userinfo
from LogInfo import LogInfo


def open_browser(chrmdvr):
    webdriver_handle = webdriver.Chrome(chrmdvr)
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


def check_results(d, err_id, arg, log):
    result = False
    try:
        ele_err = d.find_element_by_xpath(err_id)
        log.log_write(arg['Username'], arg['Password'], 'Error', ele_err.text)
    except:
        log.log_write(arg['Username'], arg['Password'], 'Pass', 'Correct Account!')
        result = True
    return result


def login_test(ele_dict, user_lst):
    wd = open_browser(ele_dict['chromedriver'])
    log = LogInfo()
    log.log_init('Username', 'Password', 'Result', 'Description')
    open_url(wd, ele_dict['url'])
    ele_tuple = find_elements(wd, ele_dict)
    for arg in user_lst:
        send_values(ele_tuple, arg)
        time.sleep(5)
        result = check_results(wd, ele_dict['err_xpath'], arg, log)
        if result:
            wd.find_element_by_xpath(ele_dict['Signout_xpath']).click()
            break
    time.sleep(10)
    log.log_close()

    wd.quit()


if __name__ == '__main__':
    user_info = Userinfo(r'UserData.xlsx')
    users_list = user_info.get_sheet_info()

    web_info = Webinfo(r'UserData.xlsx')
    ele_info = web_info.get_sheet_info()

    login_test(ele_info, users_list)
