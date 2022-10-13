class dept:
    def put(self):
        self.a=10
    def __del__(self):
        a=10
    def set(self):
        print (self.a)
     
        
d=dept()
d.put()
d.set()
d.__del__()
print(d.a)