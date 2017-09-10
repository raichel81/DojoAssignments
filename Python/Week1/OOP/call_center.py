import datetime
import itertools

class Call(object):
    newid = itertools.count().next
    def __init__(self, name, number, reason):
        self.id = Call.newid()
        self.name = name
        self.number = number
        self.time = datetime.time()
        self.reason = reason
    def display(self):
        print "Unique Id: ",self.id
        print "Caller Name: ", self.name
        print "Caller Number: ", self.number
        print "Time: ", self.time
        print "Reason for call: ", self.reason
        return self

class CallCenter(Call):
    def __init__(self, name, number,reason):
        super(CallCenter, self).__init__(name, number, reason)
        self.calls = []
        self.queue = len(self.calls)             
    def add_call(self):
        self.calls.append(self)
        print self.calls
        return self
    def remove(self):
        self.calls.remove([0])
        print self.calls
    def info(self, *calls):
        for self.call in calls:
            print "Name: "+ Call.name+ " Number:  "+ Call.number
        print self.queue

c1 = Call("Rachel", "206-471-5071", "just cause")

c1.display()
c2 = Call("Jeremy", "206-553-9430", "returning call")

c2.display()
c3 = CallCenter("Rachel", "206-471-5071", "just cause")
c3.add_call()
c3.remove()