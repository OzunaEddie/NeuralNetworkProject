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
l_count = 0
h_variation_1 =0
h_variation_2 = 0
h_variation_3 = 0
while l_count != 300 and h_variation_1 != 100 and h_variation_2 != 100 and h_variation_3 != 100: 
    ran = random.randrange(0,4)
    if ran == 0 and l_count != 300:
        training_set = ['1','0','0','1','0','0','1','0','0','1','1','1']
        rand_i = random.choice(training_set)
        if rand_i == '1':
            training_set[rand_i] = '0'
        else:
            training_set[rand_i] = '1'
        f.write("".join(training_set))
        f.write('\n')
        l_count += 1
    elif ran == 1 and h_variation_1 != 100:
        training_set = ['1','0','1','1','1','1','1','1','1','1','0','1']
        rand_i = random.choice(training_set)
        if rand_i == '1':
            training_set[rand_i] = '0'
        else:
            training_set[rand_i] = '1'
        f.write("".join(training_set))
        f.write('\n')
        h_variation_1 += 1
    elif ran == 2 and h_variation_2 != 100:
        training_set = ['1','0','1','1','0','1','1','1','1','1','0','1',]
        rand_i = random.choice(training_set)
        if rand_i == '1':
            training_set[rand_i] = '0'
        else:
            training_set[rand_i] = '1'
        f.write("".join(training_set))
        f.write('\n')
        h_variation_2 += 1
    elif ran == 3 and h_variation_3 != 100:
        training_set = ['1','0','1','1','1','1','1','0','1','1','0','1']
        rand_i = random.choice(training_set)
        if rand_i == '1':
            training_set[rand_i] = '0'
        else:
            training_set[rand_i] = '1'
        f.write("".join(training_set))
        f.write('\n')
        h_variation_3 += 1
    
    #for j in range(600):
    #training_set = ["1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1"]
    #for i in range(4, 8, 3):
     #   training_set[i] = random.choice(['0', '1'])
    #f.write("".join(training_set))
    #f.write("\n")


a = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
network = NeuralNetwork(3, 4)
network.train(a)
for i in network.random_points:
    print(i)
print(" ")
for i in network.s:
    print(i)