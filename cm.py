import xlwt


class ExcelWrite:
    def __init__(self, path):
        self.path = path
        self.excel = xlwt.Workbook()
        self.sheet = self.excel.add_sheet('Клипы')

    def __enter__(self):
        return self.sheet

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.excel.save(self.path)