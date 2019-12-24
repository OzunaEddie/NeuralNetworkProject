import random


class NeuralNetwork:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.random_points = [[0]*n for _ in range(m)]
        self.t_of_h = [[0]*8 for _ in range(m)]
        self.t_of_l = [[0]*8 for _ in range(m)]
        self.createPoints()

    def createPoints(self):
        points = random.sample(range(12), 12)
        l = 0
        k = self.n
        for i in range(self.m):
            self.random_points[i] = points[l:k]
            self.random_points[i].sort()
            l = k
            k += self.n

    def setMatrices(self, array):
        self.s = [[0]*self.n for _ in range(self.m)]
        for i in range(len(self.random_points)):
            points = self.random_points[i]
            for j in range(len(points)):
                self.s[i][j] = array[points[j]]

    def train(self, array, letter):
        self.setMatrices(array)
        if letter.lower() == 'h':
            for i in range(len(self.s)):
                index = ''.join(str(e) for e in self.s[i])
                self.t_of_h[i][self.binaryToDecimal(index)] += 1
        elif letter.lower() == 'l':
            for i in range(len(self.s)):
                index = ''.join(str(e) for e in self.s[i])
                self.t_of_l[i][self.binaryToDecimal(index)] += 1

    def binaryToDecimal(self, n):
        return int(n, 2)

    def class_l(self, array):
        self.setMatrices(array)
        self.l_total = 0
        for i in range(len(self.s)):
            index = ''.join(str(e) for e in self.s[i])
            self.l_total += self.t_of_l[i][self.binaryToDecimal(index)]

    def class_h(self, array):
        self.setMatrices(array)
        self.h_total = 0
        for i in range(len(self.s)):
            index = ''.join(str(e) for e in self.s[i])
            self.h_total += self.t_of_h[i][self.binaryToDecimal(index)]

    def belongsTo(self, array):
        self.class_h(array)
        self.class_l(array)
        answer = [None, "Actual Class:", None, "Predicted Class:", None, None]
        if self.l_total > self.h_total:
            answer[0] = array
            answer[4] = "L"
        elif self.h_total > self.l_total:
            answer[0] = array
            answer[4] = "H"
        answer[5] = True if answer[2] == answer[4] else False
        return answer


# One of the way we can generate our dataset
f = open("training.txt", "w+")
for j in range(5):
    training_set = ["1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1"]
    if j <= 2:
        index = random.choice([4, 7])
        training_set[index] = '0'
    elif j >= 2 and j <= 4:
        index = random.choice([0, 2, 9, 11])
        training_set[index] = '0'
    f.write("".join(training_set))
    f.write("\n")


h = [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1]
l = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1]
network = NeuralNetwork(3, 4)
network.train(h, 'h')
network.train(l, 'l')
for i in network.random_points:
    print(i)
print(" ")
for i in network.s:
    print(i)
print(" ")
for i in network.t_of_h:
    print(i)
print(" ")
for i in network.t_of_l:
    print(i)

print(network.belongsTo(h))
