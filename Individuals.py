class Baby():
    def __init__(self , ide ):
        self.ide = ide
        self.rcontact = [] 
        self.pcontact = []
        self.poss = .1
        self.spreadrate = .1 
        self.infected = False 
        self.recoverd = False
        self.mrate = .001
        self.alive = True
        self.days = 0
        self.dailyinf = 0
        self.totalinf = 0 
        self.type = 'baby'
class Student():
    def __init__(self , ide ):
        self.ide = ide
        self.pcontact = []
        self.rcontact = []
        self.ccontact = [] 
        self.poss = .4
        self.spreadrate = .4
        self.infected = False 
        self.recoverd = False
        self.mrate = .009
        self.alive = True
        self.days = 0
        self.dailyinf = 0
        self.totalinf = 0
        self.type = 'student'
class Teacher():
    def __init__(self , ide ):
        self.ide = ide
        self.pcontact = []
        self.rcontact = []
        self.ccontact = []
        self.poss = .3
        self.spreadrate = .3
        self.infected = False 
        self.recoverd = False
        self.mrate = .015
        self.alive = True
        self.days = 0     
        self.dailyinf = 0
        self.totalinf = 0
        self.type = 'teacher'
class Doctor():
    def __init__(self , ide ):
        self.ide = ide
        self.pcontact = []
        self.rcontact = []
        self.poss = .3
        self.spreadrate = .1
        self.infected = False 
        self.recoverd = False
        self.mrate = .015
        self.alive = True
        self.days = 0
        self.dailyinf = 0
        self.totalinf = 0
        self.type = 'doctor'
class Worker():   
    def __init__(self , ide ):
        self.ide = ide
        self.pcontact = []
        self.rcontact = []
        self.poss = .3
        self.spreadrate = .3
        self.infected = False 
        self.recoverd = False
        self.mrate = .015
        self.alive = True
        self.days = 0
        self.dailyinf = 0
        self.totalinf = 0
        self.type = 'worker'
class Old():   
    def __init__(self , ide ):
        self.ide = ide
        self.pcontact = []
        self.rcontact = []
        self.poss = .5
        self.spreadrate = .5
        self.infected = False  
        self.recoverd = False
        self.mrate = .20
        self.alive = True
        self.days = 0   
        self.dailyinf = 0
        self.totalinf = 0
        self.type = 'old'