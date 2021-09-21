class vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "[{},{}]".format(str(self.x),str(self.y))
a=vector(2,4)
print(a)


b=vector(5,2)
print(b)

def add(self,b):
    c=vector()
    c.x=self.x+b.x
    c.y=self.y+b.y
    return c
vector.add=add

c=a.add(b)
print(c)

def mul(self,s):
    return vector(self.x*s,self.y*s)

vector.mul=mul
d=a.mul(2)
print(d)

def sub(self,b):
    return self.add(b.mul(-1))
vector.sub=sub
d=d.sub(b)
print(d)
