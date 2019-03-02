import xlrd


class Webinfo(object):
    def __init__(self, path=''):
        self.xl = xlrd.open_workbook(path)
        self.sheet = self.xl.sheet_by_name('Web_info')

    def get_sheet_info(self):
        info_list = {}
        for row in range(self.sheet.nrows):
            info_list.update({self.sheet.cell(row, 0).value: self.sheet.cell(row, 1).value})
        return info_list


class Userinfo(object):
    def __init__(self, path=''):
        self.xl = xlrd.open_workbook(path)
        self.sheet = self.xl.sheet_by_name('Accounts')

    def float2str(self, val):
        if isinstance(val, float):
            val = str(int(val))
        return val

    def get_sheet_info(self):
        listkey = ['Username', 'Password']
        info_list = []
        for row in range(1, self.sheet.nrows):
            rval = [self.float2str(val) for val in self.sheet.row_values(row)]
            tmp = zip(listkey, rval)
            info_list.append(dict(tmp))
        return info_list


if __name__ == '__main__':
    uinfo = Userinfo(r'UserData.xlsx')
    info1 = uinfo.get_sheet_info()
    print(info1)

    winfo = Webinfo(r'UserData.xlsx')
    info2 = winfo.get_sheet_info()
    print(info2)
