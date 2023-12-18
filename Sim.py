import matplotlib.pyplot    as plt
import matplotlib.style     as style
import matplotlib.animation as animation
import random
from random  import randint 
from random  import choice
from random  import randint
from random  import choice
from Individuals import Student
from Individuals import Baby
from Individuals import Teacher
from Individuals import Doctor
from Individuals import Worker
from Individuals import Old
plt.style.use("Solarize_Light2")

pop = 10000
f = pop//100

def possibility(p):
    per = int(p*1000)
    randoms = randint(0,999)
    if randoms <= per:
        return True
    else:
        return False

def randomf():
    pops = [i for i in range(50*f)]
    kids = [1 for i in range(8*f)] + [2 for i in range(17*f)]
    sons = [i for i in range(42*f)]
    families = []
    while pops != []:
        a,c = choice(pops),kids.pop(randint(0,len(kids)-1))
        pops.pop(pops.index(a))
        b = choice(pops) 
        pops.pop(pops.index(b))
        family = [a,b]
        for _ in range(c):
            d = choice(sons)
            family.append(d)
            sons.pop(sons.index(d))
        families.append(family)
    return families
    
def randomConnections(types):
    if len(connect) < 10:
        a = randint(0,len(connect))
    else:
        a = randint(0,randint(0,10))
    connections = random.sample(range(len(connect)),a) 
    if types == 'w':
        connections = [connect[i] for i in connections]
    elif types == 's':
        l = connections[len(connections)//2:]
        connections = [students[i%(38*f)] for i in connections[:len(connections)//2]]
        connections = connections + [connect[i] for i in l]
    elif types == 'o':
        connections = [connect[i] for i in connections]
    return connections


babies     =  [Baby(i) for i in range(1,4*f+1)]
students   =  [Student(i) for i in range(1,38*f+1)]
teachers   =  [Teacher(i) for i in range(1,5*f+1)]
doctors    =  [Doctor(i) for i in range(1,5*f+1)]
workers    =  [Worker(i) for i in range(1,40*f+1)]
olds       =  [Old(i) for i in range(1,8*f+1)]
population =  babies + students + teachers + doctors + workers + olds 
tworkers   =  teachers + doctors + workers
kids       =  babies + students 
connect    =  students + tworkers + olds
classrooms  = list()
for i in range(len(students)//20):
    classrooms.append([students[i] for i in range(i*20 ,(i+1)*20)])

for i in range(5*f):
    teachers[i].pcontact += classrooms[i%len(classrooms)] 
    k = 0
    for j in classrooms[i%len(classrooms)]:
        copyclasse = classrooms[i%len(classrooms)].copy()
        copyclasse.pop(k) 
        classe = copyclasse + [teachers[i]]
        j.pcontact += classe
        k=k+1
families = randomf() 
for i in families:
    parents = i[:2]
    children = i[2:]
    for j in parents:
        ch = []
        for k in children:
            ch.append(kids[k])
        tworkers[j].pcontact += ch
    if len(children) == 1:
        kids[children[0]].pcontact += [tworkers[i[0]],tworkers[i[1]]]
    else:
        kids[children[0]].pcontact += [tworkers[i[0]],tworkers[i[1]],kids[children[1]]]
        kids[children[1]].pcontact += [tworkers[i[0]],tworkers[i[1]],kids[children[0]]]


zero = randint(4*f,pop-1)
population[zero].infected = True
population[zero].days     = 1
days     = 1
cases    = 1
deaths   = 0
recoverd = 0
casesl   = [1]
casest   = [1]
deathsl  = [0]
deathst  = [0]
recoverl = [0]
recovert = [0]
popl     = [pop]
print(len(population))

while cases != deaths + recoverd:
    newcases    = 0
    newdeaths   = 0
    newrecovery = 0 

    for i in tworkers:
        i.rcontact += randomConnections('w') 
    for i in students:
        i.rcontact += randomConnections('s')
    for i in olds:
        i.rcontact += randomConnections('o')
    for p in population:


        if p.infected and p.alive :
            p.days += 1
            for j in (p.rcontact+p.pcontact) : 
                if possibility(p.spreadrate) and possibility(j.poss) and j.infected == False  and not(j.recoverd) and 5 < p.days <=10:
                    j.infected  = True 
                    p.dailyinf += 1
                    p.totalinf += 1
                    newcases   += 1
                    cases      += 1
            if p.days == 15:
                if possibility(p.mrate):
                    newdeaths  += 1
                    deaths     += 1
                    p.alive     = False
                else:
                    newrecovery += 1
                    recoverd    += 1 
                    p.recoverd   = True
                    p.infected   = False
    casesl.append(newcases)
    deathsl.append(newdeaths)
    recoverl.append(newrecovery)
    casest.append(cases)
    deathst.append(deaths)
    recovert.append(recoverd)
    if days == 1:
        popl.append(pop)
    else:
        popl.append(popl[-1]-newdeaths)
    print('day: ',days)
    print('newdata: ', newcases,newdeaths,newrecovery)    
    print('alldata: ',cases,deaths,recoverd) 
    person = population[0]
    if newcases != 0:
        persontype,dailyinf = person.type,person.dailyinf
        for i in population:
            if i.dailyinf>dailyinf:
                persontype = i.type
                dailyinf   = i.dailyinf
            i.rcontact = []
            i.dailyinf = 0
        print('the most infaction were by a ',persontype, 'and he infected ',dailyinf,' people')
    days +=1 
old, olds    = 0,0
adult,adults = 0,0
young,youngs = 0,0
baby,babys   = 0,0
person = population[0]
for i in population:
    if not(i.infected) and not(i.recoverd):
        if i.type == 'old':
            olds += 1
        elif i.type == 'worker' or i.type == 'teacher' or i.type == 'doctor':
            adults += 1
        elif i.type == 'baby':
            babys += 1
        else:
            youngs +=1 
    elif i.totalinf > person.totalinf:
        person = i
    if not(i.alive):
        if i.type == 'old':
            old += 1
        elif i.type == 'worker' or i.type == 'teacher' or i.type == 'doctor':
            adult += 1
        elif i.type == 'baby':
            baby += 1
        else:
            young +=1 
print('the most infacting: ',person.type , 'and he infected ',person.totalinf,' people')
if olds + babys + youngs + adults != 0:
    print('the not infected liste: ')
    print('old people :',olds)
    print('babies :',babys)
    print('young people :',youngs)
    print('adults :',adults)
print('the deaths liste: ')
print('old people make :',(old/(old+young+baby+adult))*100)
print('babies make :',(baby/(old+young+baby+adult))*100)
print('young people make :',(young/(old+young+baby+adult))*100)
print('adults make :',(adult/(old+young+baby+adult))*100)
fig,axs  = plt.subplots(2,3)
file = open('cases.txt','w') 
casesl = casesl.copy()
file.write(str(1)+' '+str(casesl.pop(0))+' '+str(deathsl.pop(0))+' '+str(recoverl.pop(0))+' '+str(casest.pop(0))+' '+str(deathst.pop(0))+' '+str(recovert.pop(0))+'\n')
file.close()
def animate(i):
    graphs_data = open('cases.txt','r')
    lines = graphs_data.read()
    lines = lines.split('\n')
    days = []
    ys   = []
    zs   = []
    ts   = []
    sa   = []
    bs   = []
    cs   = []
    for line in lines:
        if len(line) > 1:
            x,y,z,t,a,b,c= line.split(' ')
            days.append(int(x))
            ys.append(int(y))
            zs.append(int(z))
            ts.append(int(t))
            sa.append(int(a))
            bs.append(int(b))
            cs.append(int(c))
    axs[0,0].clear()
    axs[0,1].clear()
    axs[0,2].clear()
    axs[1,0].clear()
    axs[1,1].clear()
    axs[1,2].clear()
    axs[0,0].plot(days, ys,'orange')  
    axs[0,1].plot(days, zs,'red') 
    axs[0,2].plot(days, ts,'green') 
    axs[0,0].set_xlabel('days')
    axs[0,0].set_ylabel('daily cases')
    axs[0,1].set_xlabel('days')
    axs[0,1].set_ylabel('daily deaths')
    axs[0,2].set_xlabel('days')
    axs[0,2].set_ylabel('daiy recovery')
    axs[1,0].plot(days, sa,'orange')  
    axs[1,1].plot(days, bs,'red') 
    axs[1,2].plot(days, cs,'green') 
    axs[1,0].set_xlabel('days')
    axs[1,0].set_ylabel('cases')
    axs[1,1].set_xlabel('days')
    axs[1,1].set_ylabel('deaths')
    axs[1,2].set_xlabel('days')
    axs[1,2].set_ylabel('recovery')
    plt.tight_layout()
    if casesl != []:
        graphs_data = open('cases.txt','a')
        graphs_data.write(str(int(days[-1])+1)+' '+str(casesl.pop(0))+' '+str(deathsl.pop(0))+' '+str(recoverl.pop(0))+' '+str(casest.pop(0))+' '+str(deathst.pop(0))+' '+str(recovert.pop(0))+'\n')
        file.close()
animation = animation.FuncAnimation(fig, animate, interval=200)
plt.show()