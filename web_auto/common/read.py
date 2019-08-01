
import xlrd

class ExcelUtil1():
    def __init__(self,excelPath,sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        #获取第一行作为key值
        self.keys = self.table.row_values(0)
        #获取总的行数
        self.rowNum = self.table.nrows
        #获取总列数
        self.colNum = self.table.ncols
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数据小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                #从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r
if __name__ == "__main__":
    filepath = "D:\\web_auto\\common\\datas.xlsx"
    # sheetName = "Sheet1"
    data = ExcelUtil1(filepath)
    print(data.dict_data())
