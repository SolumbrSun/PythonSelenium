import xlrd

class Helper(object):
	def readExcles(self,rowx):
		book = xlrd.open_workbook(r'E:\Python\SeleniumLearning\com\selenium\13_Encapsulation\EncapsulationLayered\data\info.xlsx', 'r')
		table = book.sheet_by_index(0)
		return table.row_values(rowx)

	def readusername(self,rowx):
		return str(self.readExcles(rowx)[0])

	def readpassword(self,rowx):
		return self.readExcles(rowx)[1]

	def exceptText(self,rowx):
		return self.readExcles(rowx)[2]


