class TreeStructure():
	def _init_(self):
		self.parent = []
		self.child = []
		self.data = []
		self.expanded = false

	def setParent(self,parent):
		for each in parent:
			self.parent.append(each)
		return 0

	def setChild(self,child):
		for each in child:
			self.child.append(each)
		return 0

	def setData(self,data):
		for each in data:
			self.data.append(each)
		return 0

	def setExpanded(self):
		self.Expanded = True
		return 0

	def getParent(self):
		parent = []
		for each in self.parent:
			parent.append(each)
		return parent

	def getChild(self):
		child = []
		for each in self.child:
			child.append(each)
		return child

	def getData(self):
		data = []
		for each in self.data:
			data.append(each)
		return data

	def getExpanded(self):
		return self.expanded
