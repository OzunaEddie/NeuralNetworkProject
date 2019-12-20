import random


class NeuralNetwork:

    def __init__(self, n, m):
        self.n = n
        self.random_points = [[0]*n]*m
        self.s = [[0]*n]*m
        self.t_of_h = [[0]*8]*m
        self.t_of_l = [[0]*8]*m
        points = random.sample(range(12), 12)
        l = 0
        k = n
        for i in range(m):
            self.random_points[i] = points[l:k]
            self.random_points[i].sort()
            l = k
            k += n

    def train(self, array):
        for i in range(len(self.random_points)):
            points = self.random_points[i]
            for j in range(len(points)):
                print(points[j])
                self.s[i][j] = array[points[j]]

    def class_l():
        return None

    def class_h():
        return None


# One of the way we can generate our dataset
f = open("training.txt", "w+")
for j in range(300):
    training_set = ["1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1"]
    for i in range(4, 8, 3):
        training_set[i] = random.choice(['0', '1'])
    f.write("".join(training_set))
    f.write("\n")


a = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
network = NeuralNetwork(3, 4)
network.train(a)
for i in network.random_points:
    print(i)
print(" ")
for i in network.s:
    print(i)
