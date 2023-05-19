import numpy as np

class Hopfield:

    def __init__(self, saved_patterns, epochs) -> None:
        self.saved_patterns = saved_patterns
        self.epochs = epochs
        self.__init_weights()

    # Matriz de pesos simetrica con la diagonal 0's
    def __init_weights(self):
        count, N = self.saved_patterns.shape
        self.weights = (1 / N) * np.matmul(self.saved_patterns.T, self.saved_patterns)
        np.fill_diagonal(self.weights, 0)

    def train(self, pattern):
        s1 = pattern
        s2 = None

        arr_patterns = []
        arr_energy = []
        arr_patterns.append(s1)
        arr_energy.append(self.__calculate_energy(s1))

        iteration = 0
        while not np.array_equal(s1, s2) and iteration < self.epochs:
            s2 = np.sign(np.matmul(self.weights, s1)).astype(int)
            
            arr_patterns.append(s2)
            arr_energy.append(self.__calculate_energy(s2))

            s1 = s2
            iteration += 1

        return np.array(list(arr_patterns)), arr_energy
    
    def __calculate_energy(self, s1):
        return -np.dot(s1.T, np.dot(np.triu(self.weights), s1))