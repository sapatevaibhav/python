class person:
	name='prince'
	roll=14
class child(person):
	def show(self):
		print(self.name)
class child2(person):
	def disp(self):
		print(self.roll)
ch=child()
ch.show()
ch2=child2()
ch2.disp()