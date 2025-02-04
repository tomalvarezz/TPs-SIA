import numpy as np
import math

def selector(population, N, K, selection_type):
    switcher = {
        "ELITE": select_elite(population, N, K),
        "ROULETTE": select_roulette(population, K),
        "UNIVERSAL": select_universal(population, K),
        "TOURNAMENT_DETERMINISTIC": select_tournament_deterministic(population, N, K),
        "TOURNAMENT_PROBABILISTIC": select_tournament_probabilistic(population, K)
    }

    return switcher.get(selection_type, "Metodo de seleccion invalido")
        

"""
Seleccionar K individuos de un conjunto de tamaño N, los ordena según el fitness
y elije cada uno n(i) veces, según n(i) = ⌈ K-i/N ⌉

"""
def select_elite(population, N, K):
    sorted_pop = sorted(population, key=lambda x: x.fitness, reverse=True)

    if (K <= N):
        return sorted_pop[:K]
    else:
        repeated_pop = []
        for i in range(K):
            repetitions = math.ceil((K - i) / N)
            for _ in range(repetitions):
                repeated_pop.append(sorted_pop[i])
        return repeated_pop

"""
Calcular aptitudes relativas pj y las aptitudes relativas acumuladas qi 
Se generan K números aleatorios y se seleccionan los K individuos xi que cumplen:

q_{i-1} < rj <= qi      Donde rj <-- UniformRandom[0,1)

"""
def select_roulette(population, K):
    fitness = np.array([subject.get_fitness() for subject in population])
    sum_fitness = np.sum(fitness)

    ps = fitness / sum_fitness      #Aptitudes relativas
    qs = np.cumsum(ps)              #Aptitudes relativas acumuladas
    rs = np.random.default_rng().uniform(0., 1., size=(K,))

    selection = []
    for ri in rs:
        for i in range(len(qs)):
            if qs[i-1] < ri <= qs[i]:
                selection.append(population[i])
                break

    return np.array(selection)

"""
Igual que en ruleta, pero la forma de calcular los rj es la siguiente:

rj = r+j/K      Donde rj <-- UniformRandom[0,1) y j en [0,(K-1)]

"""
def select_universal(population, K):
    fitness = np.array([subject.get_fitness() for subject in population])
    sum_fitness = np.sum(fitness)

    ps = fitness / sum_fitness      #Aptitudes relativas
    qs = np.cumsum(ps)              #Aptitudes relativas acumuladas
    
    r = np.random.default_rng().uniform(0., 1.)
    rj_array = []
    for j in range(K-1):
        rj_aux = (r+j)/K
        rj_array.append(rj_aux)

    selection = []
    for rj in rj_array:
        for i in range(len(qs)):
            if qs[i-1] < rj <= qs[i]:
                selection.append(population[i])
                break

    return np.array(selection)

"""
1. De la población de tamaño N, se eligen M individuos al azar.
2. De los M individuos, se elige el mejor.
3. Se repite el proceso 1. hasta conseguir los K individuos que se precisan.
"""
def select_tournament_deterministic(population, N, K):
    population_count = len(population)
    selection = []
    for _ in range(K):
        M = np.random.default_rng().choice(range(1, N))

        # Seleccionar M individuos al azar de la población
        idx = np.random.default_rng().choice(range(population_count), size=M, replace=True)
        competitors = [population[i] for i in idx]

        # Seleccionar de los M individuos al ganador (mayor aptitud)
        winner = max(competitors, key=lambda subject: subject.get_fitness())
        selection.append(winner)

    return np.array(selection)


"""
1. Se elige un valor de Threshold en [0.5, 1] aleatorio.
2. De la población de tamaño N, se eligen 2 individuos al azar.
3. Se toma un valor r al azar uniformemente en [0,1].
    1. Si r < Threshold se selecciona el más apto.
    2. Caso contrario, se selecciona el menos apto.
4. Se repite el proceso hasta conseguir los K individuos que se precisan.
"""
def select_tournament_probabilistic(population, K):
    threshold = np.random.default_rng().uniform(0.5, 1.)
    population_count = len(population)
    selection = []
    for _ in range(K):
        # Seleccionar 2 individuos al azar de la población
        idx = np.random.default_rng().choice(range(population_count), size=2, replace=True)
        competitors = [population[i] for i in idx]

        r = np.random.default_rng().uniform(0., 1.)

        if(r < threshold):
            winner = max(competitors, key=lambda subject: subject.get_fitness())
        else:
            winner = min(competitors, key=lambda subject: subject.get_fitness())
        
        selection.append(winner)

    return np.array(selection)
