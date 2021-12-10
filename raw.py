class info:
	def __init__(self, roll, cgpa):
		self.roll = str(roll)
		self.cgpa = float(cgpa)
	def clean_roll(self):
		if(self.roll[-1] == '5'):
			li = list(self.roll)
			li[-1] = 'S'
			self.roll = "".join(li)
		for i, letter in enumerate(self.roll):
			if letter == 'O':
				li = list(self.roll)
				li[i] = '0'
				self.roll = "".join(li) 


raw = open('test', 'r')
lines = raw.readlines()

pro = open('proc', 'w')

listOfInfo = []

for line in lines:
	array = line.split()
	listOfInfo.append(info(array[0], array[-1]))

for each in listOfInfo:
	each.clean_roll()
	pro.write(f"{each.roll},{each.cgpa}\n")

raw.close()
pro.close()

