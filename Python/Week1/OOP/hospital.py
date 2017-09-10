import itertools

class Patient(object):
    newid = itertools.count().next
    def __init__(self, name, allergies):
        self.id = Patient.newid()
        self.name = name
        self.allergies = allergies
        self.bed = None
    def display(self):
        print "Unique Id: ",self.id
        print "Patient Name: ", self.name
        print "Allergies: ", self.allergies
        print "Bed #: ", self.bed
        print
        return self
class Hospital(object):
    def __init__(self,name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.beds = [None]*capacity            
    def admit_patient(self, patient):
        for index, bed in enumerate(self.beds):
            if bed == None:
                print "Patient has been admitted"
                self.patients.append(patient)
                patient.bed = index
                self.beds[index] = patient
                print "Bed number:", patient.bed
                print
                return self
        print "Sorry, hospital is full."
        print
        return self
    def info(self):
        for patient in self.patients:
            print "Name: ", patient.name
            print "Bed number:  ", patient.bed
        print "Avalable rooms left: ", self.capacity - len(self.patients)
        print
        return self
    def discharge_patient(self, name):
        for patient in self.patients:
            if patient.name == name:
                self.patients.remove(patient)
                self.beds[patient.bed]= None
                patient.bed = None
                print "Patient has been discharged"
                print "Avalable rooms left: ", self.capacity - len(self.patients)
                print


p1 = Patient("Bob", ['cats', 'pollen', 'dust'])
p2 = Patient("Sue", ['trees'])
p3 = Patient("Helen", [])

h1 = Hospital("Memorial", 2)

p1.display()
p2.display()
p3.display()
h1.admit_patient(p1).info()
h1.admit_patient(p2).info().discharge_patient("Bob")
h1.admit_patient(p3).info()
p3.display()
p1.display()

