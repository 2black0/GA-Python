# Simple Genetic Algorithm on Python
This project to show the genetic algorithm process in python

Why python? cos I love it

dont love python? its your problem :P

## Requirement
```
pip install numpy
```

## Explanation of Algorithm
Flowchart of GA

![Flowchart of GA](https://cdn-images-1.medium.com/max/1600/1*HP8JVxlJtOv14rGLJfXEzA.png)

### 1. Initialize Population
> What is population? Population is a collection of genes

> What is gen? its an individual in the population

for simple explanation, I have an example :
``` 
gen = 'Hello World!'
Population = ('Hello World!', 'Hello Wordd!', 'Hello Morth!')
```
so how to create or initialize population? just create random gen and collect it save it in a variable. This is the code how to generate new random gen and collect it into a population. The datatype of population is a dict, for matlab just use struct. Before save it into a population we need to calculate the fitness between a gen with the target. If a gen is match with the target, the value of fitness is 100. So in the population we will a pair of gen and its fitness
```
# generate new gen
def create_gen(panjang_target):
    random_number = np.random.randint(32, 126, size=panjang_target)
    gen = ''.join([chr(i) for i in random_number])
    return gen

# calculate fitness of gen
def calculate_fitness(gen, target, panjang_target):
    fitness = 0
    for i in range (panjang_target):
        if gen[i:i+1] == target[i:i+1]:
            fitness += 1
    fitness = fitness / panjang_target * 100
    return fitness

# create population
def create_population(target, max_population, panjang_target):
    populasi = {}
    for i in range(max_population):
        gen = create_gen(panjang_target)
        genfitness = calculate_fitness(gen, target, panjang_target)
        populasi[gen] =  genfitness
    return populasi
```

### 2. Selection

### 3. Crossover

### 4. Mutation

### 5. Evaluation

### 6. Regeneration of Population
