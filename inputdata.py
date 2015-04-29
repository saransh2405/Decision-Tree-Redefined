class input():
	def _init_(self):
		self.rows = 0
		self.columns = 0
		self.datass = [""]


	def setRows(self,rows):
		self.rows = rows
		return 0

	def setColumns(self,columns):
		self.columns = columns
		return 0

	def setData(self,data):
		self.datass=[]
		for each in data:
			self.datass.append(each.split(" "))
		return 0


	def getRows(self):
		return self.rows

	def getColumns(self):
		return self.columns

	def getData(self):
		return self.datass



	