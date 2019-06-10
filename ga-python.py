import numpy as np
import datetime

# generate new gen
def create_gen(panjang_target):
    random_number = np.random.randint(32, 126, size=panjang_target)
    gen = ""    .join([chr(i) for i in random_number])
    return gen

# calculate fitness of gen
def calculate_fitness(gen, target, panjang_target):
    fitness = 0
    for i in range (panjang_target):
        if gen[i:i+1] == target[i:i+1]:
            fitness += 1
        else:
            fitness = fitness
    fitness = fitness / panjang_target * 100
    return fitness

# create population
def create_population(target, besar_populasi, panjang_target):
    populasi = {}
    for i in range(besar_populasi):
        gen = create_gen(panjang_target)
        genfitness = calculate_fitness(gen, target, panjang_target)
        populasi[gen] =  genfitness
    return populasi

# selection process
def selection(populasi):
    pop = dict(populasi)
    parent = {}
    for i in range(2):
        gen = max(pop, key=pop.get)
        genfitness = pop[gen]
        parent[gen] = genfitness
        if i == 0:
            del pop[gen]
    return parent

# crossover
def crossover(parent, target, panjang_target):
    child = {}
    cp = round(len(list(parent)[0])/2)
    for i in range(2):
        gen = list(parent)[i][:cp] + list(parent)[1-i][cp:]
        genfitness = calculate_fitness(gen, target, panjang_target)
        child[gen] = genfitness
    return child

# mutation
def mutation(child, target, laju_mutasi, panjang_target):
    mutant = {}
    for i in range(len(child)):     
        data = list(list(child)[i])
        for j in range(len(data)):
            if np.random.rand(1) <= laju_mutasi:
                ch = chr(np.random.randint(32, 126))
                #print('data ke :', i,',', j, 'data awal :', data[j], 'data akhir :', ch,'\n')
                data[j] = ch
        gen = ''.join(data)
        genfitness = calculate_fitness(gen, target, panjang_target)
        mutant[gen] = genfitness
    return mutant

# create new population with new best gen
def regeneration(mutant, populasi):
    for i in range(len(mutant)):
        bad_gen = min(populasi, key=populasi.get)
        del populasi[bad_gen]
    populasi.update(mutant)
    return populasi

# get best fitness in a population
def bestfitness(parent):
    fitness = parent[max(parent, key=parent.get)]
    return fitness

# display function
def display(parent):
    timeDiff=datetime.datetime.now()-startTime
    data = list(parent)
    print('{}\t{}%\t{}'.format(data[0],round(parent[data[0]],2),timeDiff))

# main program
target = 'Hello World!'
besar_populasi = 10
laju_mutasi = 0.2

print('Target Word :', target)
print('Max Population :', besar_populasi)
print('Mutation Rate :', laju_mutasi)

panjang_target = len(target)
startTime=datetime.datetime.now()
print('{}\t{}\t{}'.format('The Best','Fitness','Time'))
print('{}\t{}\t{}'.format('--------','-------','----'))
populasi = create_population(target, int(besar_populasi), panjang_target)
parent = selection(populasi)

display(parent)
while 1:
    child = crossover(parent, target, panjang_target)
    mutant = mutation(child, target, float(laju_mutasi), panjang_target)
    if bestfitness(parent) >= bestfitness(mutant):
        continue
    populasi = regeneration(mutant, populasi)
    parent = selection(populasi)
    display(parent)
    if bestfitness(mutant) >= 100:
        print('-------------------------')
        print('Target found, End Process')
        break