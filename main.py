import treestructure as ts
import inputdata as id
import math



def finddistinct(targetset):
	result = []
	for trow in targetset:
		if trow not in result:
			result.append(trow)
	return result


def calLogVal(logs):
	result = 0.0
	for each in logs:
		result += each*math.log((1/each),2)

	return result


def check(ts):
	checkdata = []
	for i in range(int(instance.getColumns())-1):
		test = []
		for each in ts:
			test.append(instance.getData()[int(each)][i])

		if(len(finddistinct(test))==1):
			set = 1
		else:
			return 0

	return set
	

def calProbability(targetset):
	probs = []
	prob = []
	w = 0.0
	prob = finddistinct(targetset)
	for each in prob:
		probs.append(float(targetset.count(each))/len(targetset))

	return probs


def makeset(erows,trow):
	distincts = finddistinct(erows)
	x = "null"
	p=0.0
	entropy = 0.0
	for each in distincts:
		i=0
		pr = []
		for erow in erows:
			if each is erow:
				if each == x:
					pr.append(trow[i])
				else:
					p = float(erows.count(x))/len(erows)
					entropy += p*calLogVal(calProbability(pr))
					pr = []
					pr.append(trow[i])
				x=each
			else:
				pass

			i+=1
		p = float(erows.count(x))/len(erows)
		entropy += p*calLogVal(calProbability(pr))
	return entropy


def gain(dataset):
	data = []
	for each in dataset:
		data.append(instance.getData()[int(each)][int(instance.getColumns())-1])
	return calLogVal(calProbability(data))


def calEntropy(targetdataset):
	entropy = []

	for columnnumber in range(0,int(instance.getColumns())-1):
		erow = []
		trow = []
		for rownumber in range(0,int(instance.getRows())):
			if rownumber in targetdataset:
				erow.append(instance.getData()[rownumber][columnnumber])
				trow.append(instance.getData()[rownumber][int(instance.getColumns())-1])

		entropy.append(makeset(erow,trow))
	
	return entropy

		
def min(dataset):
	min = 2.0
	for each in dataset:
		if each < min:
			min = each
	return min

def max(dataset):
	max = -1
	i=0
	index=0
	for each in dataset:
		if each > max:
			max = each
			i = index
		index = index + 1
	return i

def breakset(t):
	for i in range(len(t)):
		for y in range(len(t)):
			temp = [[0,0]]
			if t[i][1]<t[y][1]:
				temp[0][0] = t[y][0]
				temp[0][1] = t[y][1]
				t[y][0] = t[i][0]
				t[y][1] = t[i][1]
				t[i][0] = temp[0][0]
				t[i][1] = temp[0][1]

	q=[]
	p=[]
	x = t[0][1]
	for each in t:
		if each[1] == x:
			q.append(each)
		else:
			p.append(q)
			q=[]
			q.append(each)
		x=each[1]
	p.append(q)
	return p

def main(instance):
	input1 = raw_input("Enter names of the files dataset input-partition output-partition\n")
	datafile = input1.split(" ")[0]
	inputfile1 = input1.split(" ")[1]
	output = input1.split(" ")[2]
	


	f1 = open(datafile,"r")
	x = f1.read()
	f1.close()

	f1 = open(inputfile1,"r")
	y = f1.read()
	f1.close()
	targetdataset1 = []
	rows = x.split("\n")[0].split(" ")[0]
	columns = x.split("\n")[0].split(" ")[1]
	data = x.split("\n")[1:]
	targetdataset = []
	nodes = y.split("\n")
	name = []
	targetdataset1 = []

	instance.setRows(rows)
	instance.setColumns(columns)
	instance.setData(data)

	nontargetdataset1 = []
	name = []
	nontargetname = []
	targetname=[]
	fields = []
	for node in nodes:
		name.append(node.split(" ")[0])
		fields = node.split(" ")[1:]
		targetdataset = []
		for field in fields:
			targetdataset.append(int(field)-1)
		target = []
		for each in targetdataset:
			target.append(instance.getData()[int(each)][int(instance.getColumns())-1])

		if(len(finddistinct(target))>1) and (check(targetdataset) != 1):
			targetdataset1.append(targetdataset)
			targetname.append(node.split(" ")[0])
		else:
			nontargetdataset1.append(targetdataset)
			nontargetname.append(node.split(" ")[0])


	nodes = []
	line = ""
	index = 0
	for each in targetdataset1:
		line = targetname[index]
		for i in each:
			line = line + " "+str(i+1)
		index = index + 1
		nodes.append(line)
		line = ""


	line = ""
	index = 0	
	for each in nontargetdataset1:
		line = line + nontargetname[index]
		for i in each:
			line = line + " "+str(i+1)
		index = index + 1
		nodes.append(line)
		line = ""
	

	if targetdataset1 == []:
		print "Cannot split any further"

	else:
		e = []
		t = []
		s = []
	 	for targetdataset in targetdataset1:
	 		t.append(gain(targetdataset))
			e.append(calEntropy(targetdataset))
			s.append(len(targetdataset))


		index = 0
		fvalue = []
		for gains in t:
			fvalue.append((s[index])*(gains-min(e[index])))
			index = index + 1 


		splitcase = max(fvalue)
		children = []
		c=[]
		name = nodes[splitcase].split(" ")[0]
		for child in nodes[splitcase].split(" ")[1:]:
			c=[]
			c.append(child)
			c.append(instance.getData()[(int(child)-1)][e[splitcase].index(min(e[splitcase]))])
			children.append(c)
		
		index = 0
		f1 = open(output,"w")
		line = ""
		for each in nodes:
			if each.split(" ")[0] == name:
				pass
			else:
				line = line + each +"\n"


		splitnames = ""
		for child in breakset(children):
			z = name+str(index)
			splitnames= splitnames+z+" "
			for each in child:
				z=z+" "+ each[0]
			line = line + z+"\n"
			index=index+1

		line = line.strip("\n")
		f1.write(line)
		f1.close()
		print "Partition",name,"was replaced with partitions",splitnames,"using Feature ",e[splitcase].index(min(e[splitcase]))+1


if __name__ == '__main__':
	instance = id.input()
	main(instance)