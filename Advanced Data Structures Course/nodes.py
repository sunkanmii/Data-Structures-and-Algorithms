class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Tue')
e3 = daynames('Wed')
e4 = daynames('Thur')
e5 = daynames('Fri')
e6 = daynames('Sat')

e1.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
e5.nextval = e6

# Traversing through nodes
thisvalue = e1
while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval