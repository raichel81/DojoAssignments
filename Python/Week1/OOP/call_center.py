import datetime
import itertools

class Call(object):
    newid = itertools.count().next
    def __init__(self, name, number, reason):
        self.id = Call.newid()
        self.name = name
        self.number = number
        self.time = datetime.datetime.now()
        self.reason = reason
    def display(self):
        print "Unique Id: ",self.id
        print "Caller Name: ", self.name
        print "Caller Number: ", self.number
        print "Time: ", self.time
        print "Reason for call: ", self.reason
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = len(self.calls)             
    def add_call(self, call):
        self.calls.append(call)
        self.queue +=1
        return self
    def remove(self):
        self.calls.remove(self.calls[0])
        self.queue -=1
    def info(self):
        for call in self.calls:
            print "Name: "+ call.name+ " Number:  "+ call.number
        print self.queue
    def delete_by_number(self, number):
        for call in self.calls:
            if call.number == number:
                self.calls.remove(call)

c1 = Call("Rachel", "206-5555", "just cause")

c1.display()
c2 = Call("Jeremy", "206-7777", "returning call")

c2.display()
call_center1 = CallCenter()
call_center1.add_call(c2)
call_center1.add_call(c1)

call_center1.info()
call_center1.delete_by_number("206-5555")
call_center1.info()