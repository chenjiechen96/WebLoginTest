import time
import xlsxwriter


class LogInfo(object):
    def __init__(self, path=''):
        filename = path + time.strftime('%Y-%m-%d', time.gmtime())
        self.row = 0
        self.log = xlsxwriter.Workbook(path+filename+'.xlsx')
        self.sheet = self.log.add_worksheet('Report')

    def log_init(self, *title):
        self.sheet.set_column('A:D', 30)
        self.log_write(*title)

    def log_write(self, *args):
        col = 0
        for val in args:
            self.sheet.write_string(self.row, col, val)
            col += 1
        self.row += 1

    def log_close(self):
        self.log.close()


if __name__ == '__main__':
    log = LogInfo()
    log.log_init('Username', 'Password', 'Result', 'Description')
    log.log_write('aaa', 'bbb', 'ccc', 'ddd')
    log.log_close()
