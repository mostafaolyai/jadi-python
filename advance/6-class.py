class ClassRoom:
    def __init__(self, w, l, a):
        self.w = w
        self.l = l
        self.a = a

    def average_w(self):
        return sum(self.w) / len(self.w)

    def average_l(self):
        return sum(self.l) / len(self.l)

    def info(self):
        print(f"{self.average_w()} {self.average_l()} {sum(self.a) / len(self.a)}")

count = int(input())

aW=[]
aL=[]
aA=[]
bW=[]
bL=[]
bA=[]

aW=list(map(lambda x: int(x),input('Weights of class A: ').split(' ')))
aL=list(map(lambda x: int(x),input('Length of class A: ').split(' ')))
aA=list(map(lambda x: int(x),input('Ages of class A: ').split(' ')))

bW=list(map(lambda x: int(x),input('Weights of class B: ').split(' ')))
bL=list(map(lambda x: int(x),input('Length of class B: ').split(' ')))
bA=list(map(lambda x: int(x),input('Ages of class B: ').split(' ')))

class_a = ClassRoom(aW,aL,aA)
class_b = ClassRoom(bW,bL,bA)

class_a.info()
class_b.info()

if class_a.average_w() > class_b.average_w():
    print('A')
elif class_a.average_w() < class_b.average_w():
    print('B')
else: 
    if class_a.average_l() > class_b.average_l():
        print('A')
    elif class_a.average_l() < class_b.average_l():
        print('B')
    else: print('same')

